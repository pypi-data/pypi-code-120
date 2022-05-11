""" Module to define various calculation types as Enums for VASP """
from itertools import product
from pathlib import Path

from monty.serialization import loadfn

from emmet.core.utils import get_enum_source

_RUN_TYPE_DATA = loadfn(str(Path(__file__).parent.joinpath("run_types.yaml").resolve()))
_TASK_TYPES = [
    "NSCF Line",
    "NSCF Uniform",
    "Dielectric",
    "DFPT",
    "DFPT Dielectric",
    "NMR Nuclear Shielding",
    "NMR Electric Field Gradient",
    "Static",
    "Structure Optimization",
    "Deformation",
    "Unrecognized",
]

_RUN_TYPES = (
    [
        rt
        for functional_class in _RUN_TYPE_DATA
        for rt in _RUN_TYPE_DATA[functional_class]
    ]
    + [
        f"{rt}+U"
        for functional_class in _RUN_TYPE_DATA
        for rt in _RUN_TYPE_DATA[functional_class]
    ]
    + ["LDA", "LDA+U"]
)


run_type_enum = get_enum_source(
    "RunType",
    "VASP calculation run types",
    dict(
        {
            "_".join(rt.split()).replace("+", "_").replace("-", "_"): rt
            for rt in _RUN_TYPES
        }
    ),
)
task_type_enum = get_enum_source(
    "TaskType",
    "VASP calculation task types",
    {"_".join(tt.split()): tt for tt in _TASK_TYPES},
)
calc_type_enum = get_enum_source(
    "CalcType",
    "VASP calculation types",
    {
        f"{'_'.join(rt.split()).replace('+','_').replace('-','_')}_{'_'.join(tt.split())}": f"{rt} {tt}"
        for rt, tt in product(_RUN_TYPES, _TASK_TYPES)
    },
)


with open(Path(__file__).parent / "enums.py", "w") as f:
    f.write(
        """\"\"\"
Autogenerated Enums for VASP RunType, TaskType, and CalcType
Do not edit this by hand. Edit generate.py or run_types.yaml instead
\"\"\"
from emmet.core.utils import ValueEnum

"""
    )
    f.write(run_type_enum)
    f.write("\n\n")
    f.write(task_type_enum)
    f.write("\n\n")
    f.write(calc_type_enum)
    f.write("\n")
