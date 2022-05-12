import json
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, validator

from .annotations import *
from .ids import get_pecha_id, get_uuid


class LayerEnum(Enum):
    index = "index"

    book_title = "BookTitle"
    sub_title = "SubTitle"
    book_number = "BookNumber"
    poti_title = "PotiTitle"
    author = "Author"
    chapter = "Chapter"

    topic = "Text"
    sub_topic = "SubText"

    pagination = "Pagination"
    citation = "Citation"
    correction = "Correction"
    error_candidate = "ErrorCandidate"
    peydurma = "Peydurma"
    sabche = "Sabche"
    tsawa = "Tsawa"
    yigchung = "Yigchung"
    archaic = "Archaic"
    durchen = "Durchen"
    footnote = "Footnote"
    segment = "Segment"


class InitialCreationEnum(Enum):
    ocr = "ocr"
    ebook = "ebook"
    input = "input"


def _get_annotation_class(layer_name: LayerEnum):
    """Maps LayerEnum to Annotation class"""
    if layer_name == LayerEnum.book_title:
        return BaseAnnotation
    elif layer_name == LayerEnum.sub_title:
        return BaseAnnotation
    elif layer_name == LayerEnum.book_number:
        return BaseAnnotation
    elif layer_name == LayerEnum.poti_title:
        return BaseAnnotation
    elif layer_name == LayerEnum.author:
        return BaseAnnotation
    elif layer_name == LayerEnum.chapter:
        return BaseAnnotation
    elif layer_name == LayerEnum.topic:
        return BaseAnnotation
    elif layer_name == LayerEnum.sub_topic:
        return BaseAnnotation
    elif layer_name == LayerEnum.pagination:
        return Pagination
    elif layer_name == LayerEnum.citation:
        return Citation
    elif layer_name == LayerEnum.correction:
        return Correction
    elif layer_name == LayerEnum.error_candidate:
        return ErrorCandidate
    elif layer_name == LayerEnum.peydurma:
        return Pedurma
    elif layer_name == LayerEnum.sabche:
        return Sabche
    elif layer_name == LayerEnum.tsawa:
        return Tsawa
    elif layer_name == LayerEnum.yigchung:
        return Yigchung
    elif layer_name == LayerEnum.archaic:
        return Archaic
    elif layer_name == LayerEnum.durchen:
        return Durchen
    elif layer_name == LayerEnum.footnote:
        return Footnote
    elif layer_name == LayerEnum.segment:
        return Segment
    else:
        return BaseAnnotation


class Layer(BaseModel):
    id: str = None
    annotation_type: LayerEnum
    revision: str = "00001"
    annotations: Dict = {}

    @validator("id", pre=True, always=True)
    def set_id(cls, v):
        return v or get_uuid()

    @validator("revision")
    def revision_must_int_parsible(cls, v):
        assert v.isdigit(), "must integer parsible like `00002`"
        return v

    def bump_revision(self):
        self.revision = f"{int(self.revision)+1:05}"

    def reset(self):
        self.revision = "00001"
        self.annotations = {}

    def get_annotations(self):
        """Yield Annotation Objects"""
        for ann_id, ann_dict in self.annotations.items():
            ann_class = _get_annotation_class(self.annotation_type)
            ann_dict["id"] = ann_id
            ann = ann_class.parse_obj(ann_dict)
            yield ann

    def get_annotation(self, annotation_id: str) -> Optional[BaseAnnotation]:
        """Retrieve annotation of id `annotation_id`"""
        ann_dict = self.annotations.get(annotation_id)
        if not ann_dict:
            return
        ann_class = _get_annotation_class(self.annotation_type)
        ann = ann_class.parse_obj(ann_dict)
        return ann

    def set_annotation(self, ann: BaseAnnotation):
        """Add or Update annotation `ann` to the layer"""
        self.annotations[ann.id] = json.loads(ann.json())

    def remove_annotation(self, annotation_id: str):
        """Delete annotaiton of `annotation_id` from the layer"""
        if annotation_id in self.annotations:
            del self.annotations[annotation_id]


class PechaMetaData(BaseModel):
    id: str = None
    initial_creation_type: InitialCreationEnum
    source_metadata: Optional[Dict] = {}
    created_at: datetime = None
    last_modified_at: datetime = None
    statistics: Dict[str, Union[int, float, str]] = {}
    quality: Dict[str, Union[int, float]] = {}

    @validator("id", pre=True, always=True)
    def set_id(cls, v):
        return v or get_pecha_id()

    @validator("created_at", pre=True, always=True)
    def set_created_date(cls, v):
        return v or datetime.now()

    @validator("last_modified_at", pre=True, always=True)
    def set_last_modified_date(cls, v):
        return v or datetime.now()

    def update_last_modified_date(self):
        self.last_modified_at = datetime.now()


class SpanINFO(BaseModel):
    text: str
    layers: Dict[LayerEnum, List[BaseAnnotation]]
    metadata: PechaMetaData
