from datetime import datetime
from itertools import chain
from math import ceil
from typing import Optional, Iterable, Iterator, List, Dict

from maggma.builders import Builder
from maggma.core import Store
from maggma.utils import grouper

from emmet.core.qchem.task import TaskDocument
from emmet.core.qchem.molecule import MoleculeDoc, evaluate_lot
from emmet.core.molecules.bonds import BondingDoc, BOND_METHODS
from emmet.core.utils import jsanitize
from emmet.builders.settings import EmmetBuildSettings


__author__ = "Evan Spotte-Smith"

SETTINGS = EmmetBuildSettings()


class BondingBuilder(Builder):
    """
    The BondingBuilder defines the bonds in a MoleculeDoc.

    Various methods can be used to define bonding, including:
        - OpenBabelNN + metal_edge_extender: Combining the bond detection algorithms in OpenBabel (OpenBabelNN in
            pymatgen) with a heuristic to add metal coordinate bonds (metal_edge_extender
            in pymatgen)
        - critic2: Using critical points of the electron density to define bonds
        - nbo: Using Natural Bonding Orbital analysis to define bonds and other
            interatomic interactions

    NOTE: Only NBO7 can be used to generate bonding. Bonding (especially when metals
        are involved) is unreliable with earlier version of NBO!

    This builder will attempt to build documents for each molecule with each method.
    For each molecule-method combination, the highest-quality data available (based
    on level of theory and electronic energy) will be used.

    The process is as follows:
        1. Gather MoleculeDocs by formula
        2. For each molecule, sort all associated tasks by level of theory and electronic energy
        2. For each method:
            2.1. Find task docs with necessary data to define bonding by that method
            2.2. Take best (defined by level of theory and electronic energy) task
            2.3. Convert TaskDoc to BondingDoc
    """

    def __init__(
        self,
        tasks: Store,
        molecules: Store,
        bonds: Store,
        query: Optional[Dict] = None,
        methods: Optional[List] = None,
        settings: Optional[EmmetBuildSettings] = None,
        **kwargs,
    ):

        self.tasks = tasks
        self.molecules = molecules
        self.bonds = bonds
        self.query = query if query else dict()
        self.methods = methods if methods else BOND_METHODS
        self.settings = EmmetBuildSettings.autoload(settings)
        self.kwargs = kwargs

        super().__init__(sources=[tasks, molecules], targets=[bonds])

    def ensure_indexes(self):
        """
        Ensures indices on the collections needed for building
        """

        # Basic search index for tasks
        self.tasks.ensure_index("task_id")
        self.tasks.ensure_index("last_updated")
        self.tasks.ensure_index("state")
        self.tasks.ensure_index("formula_alphabetical")

        # Search index for molecules
        self.molecules.ensure_index("molecule_id")
        self.molecules.ensure_index("last_updated")
        self.molecules.ensure_index("task_ids")
        self.molecules.ensure_index("formula_alphabetical")

        # Search index for charges
        self.bonds.ensure_index("molecule_id")
        self.bonds.ensure_index("method")
        self.bonds.ensure_index("task_id")
        self.bonds.ensure_index("last_updated")
        self.bonds.ensure_index("formula_alphabetical")

    def prechunk(self, number_splits: int) -> Iterable[Dict]:  # pragma: no cover
        """Prechunk the builder for distributed computation"""

        temp_query = dict(self.query)
        temp_query["deprecated"] = False

        self.logger.info("Finding documents to process")
        all_mols = list(
            self.molecules.query(
                temp_query, [self.molecules.key, "formula_alphabetical"]
            )
        )

        processed_docs = set([e for e in self.bonds.distinct("molecule_id")])
        to_process_docs = {d[self.molecules.key] for d in all_mols} - processed_docs
        to_process_forms = {
            d["formula_alphabetical"]
            for d in all_mols
            if d[self.molecules.key] in to_process_docs
        }

        N = ceil(len(to_process_forms) / number_splits)

        for formula_chunk in grouper(to_process_forms, N):
            yield {"query": {"formula_alphabetical": {"$in": list(formula_chunk)}}}

    def get_items(self) -> Iterator[List[Dict]]:
        """
        Gets all items to process into bonding documents.
        This does no datetime checking; relying on on whether
        task_ids are included in the bonds Store

        Returns:
            generator or list relevant tasks and molecules to process into documents
        """

        self.logger.info("Bonding builder started")
        self.logger.info("Setting indexes")
        self.ensure_indexes()

        # Save timestamp to mark buildtime
        self.timestamp = datetime.utcnow()

        # Get all processed molecules
        temp_query = dict(self.query)
        temp_query["deprecated"] = False

        self.logger.info("Finding documents to process")
        all_mols = list(
            self.molecules.query(
                temp_query, [self.molecules.key, "formula_alphabetical"]
            )
        )

        processed_docs = set([e for e in self.bonds.distinct("molecule_id")])
        to_process_docs = {d[self.molecules.key] for d in all_mols} - processed_docs
        to_process_forms = {
            d["formula_alphabetical"]
            for d in all_mols
            if d[self.molecules.key] in to_process_docs
        }

        self.logger.info(f"Found {len(to_process_docs)} unprocessed documents")
        self.logger.info(f"Found {len(to_process_forms)} unprocessed formulas")

        # Set total for builder bars to have a total
        self.total = len(to_process_forms)

        for formula in to_process_forms:
            mol_query = dict(temp_query)
            mol_query["formula_alphabetical"] = formula
            molecules = list(self.molecules.query(criteria=mol_query))

            yield molecules

    def process_item(self, items: List[Dict]) -> List[Dict]:
        """
        Process the tasks into BondingDocs

        Args:
            tasks List[Dict] : a list of MoleculeDocs in dict form

        Returns:
            [dict] : a list of new bonding docs
        """

        mols = [MoleculeDoc(**item) for item in items]
        formula = mols[0].formula_alphabetical
        mol_ids = [m.molecule_id for m in mols]
        self.logger.debug(f"Processing {formula} : {mol_ids}")

        bonding_docs = list()

        for mol in mols:
            correct_charge_spin = [
                e
                for e in mol.entries
                if e["charge"] == mol.charge
                and e["spin_multiplicity"] == mol.spin_multiplicity
            ]

            sorted_entries = sorted(
                correct_charge_spin,
                key=lambda x: (sum(evaluate_lot(x["level_of_theory"])), x["energy"]),
            )

            for method in self.methods:
                # For each method, grab entries that have the relevant data
                if method == "OpenBabelNN + metal_edge_extender":
                    relevant_entries = sorted_entries
                else:
                    relevant_entries = [
                        e
                        for e in sorted_entries
                        if e.get(method) is not None
                        or e["output"].get(method) is not None
                    ]

                if method == "nbo":
                    # Only allow NBO7 to be used. No earlier versions can be
                    # relied upon for bonding
                    relevant_entries = [
                        e
                        for e in relevant_entries
                        if e["orig"]["rem"].get("run_nbo6", False)
                    ]

                if len(relevant_entries) == 0:
                    continue

                # Grab task document of best entry
                best_entry = relevant_entries[0]
                task = best_entry["task_id"]

                task_doc = TaskDocument(**self.tasks.query_one({"task_id": int(task)}))

                doc = BondingDoc.from_task(
                    task_doc,
                    molecule_id=mol.molecule_id,
                    preferred_methods=[method],
                    deprecated=False,
                )

                bonding_docs.append(doc)

        self.logger.debug(f"Produced {len(bonding_docs)} bonding docs for {formula}")

        return jsanitize([doc.dict() for doc in bonding_docs], allow_bson=True)

    def update_targets(self, items: List[List[Dict]]):
        """
        Inserts the new documents into the charges collection

        Args:
            items [[dict]]: A list of documents to update
        """

        docs = list(chain.from_iterable(items))  # type: ignore

        # Add timestamp
        for item in docs:
            item.update(
                {
                    "_bt": self.timestamp,
                }
            )

        molecule_ids = list({item["molecule_id"] for item in docs})

        if len(items) > 0:
            self.logger.info(f"Updating {len(docs)} bonding documents")
            self.bonds.remove_docs({self.bonds.key: {"$in": molecule_ids}})
            # Neither molecule_id nor method need to be unique, but the combination must be
            self.bonds.update(
                docs=docs,
                key=["molecule_id", "method"],
            )
        else:
            self.logger.info("No items to update")
