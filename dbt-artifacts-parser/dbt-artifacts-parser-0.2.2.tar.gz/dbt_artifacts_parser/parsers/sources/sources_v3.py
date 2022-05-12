# generated by datamodel-codegen:
#   filename:  sources_v3.json
#   timestamp: 2022-03-01T06:21:38+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import Extra

from dbt_artifacts_parser.parsers.base import BaseParserModel


class FreshnessMetadata(BaseParserModel):

    class Config:
        extra = Extra.forbid

    dbt_schema_version: Optional[
        str] = 'https://schemas.getdbt.com/dbt/sources/v3.json'
    dbt_version: Optional[str] = '1.0.0b2'
    generated_at: Optional[datetime] = '2021-11-02T20:18:06.796684Z'
    invocation_id: Optional[Optional[str]] = None
    env: Optional[Dict[str, str]] = {}


class Status(Enum):
    runtime_error = 'runtime error'


class SourceFreshnessRuntimeError(BaseParserModel):

    class Config:
        extra = Extra.forbid

    unique_id: str
    error: Optional[Optional[Union[str, int]]] = None
    status: Status


class Status1(Enum):
    pass_ = 'pass'
    warn = 'warn'
    error = 'error'
    runtime_error = 'runtime error'


class PeriodEnum(Enum):
    minute = 'minute'
    hour = 'hour'
    day = 'day'


class Time(BaseParserModel):

    class Config:
        extra = Extra.forbid

    count: Optional[Optional[int]] = None
    period: Optional[Optional[PeriodEnum]] = None


class TimingInfo(BaseParserModel):

    class Config:
        extra = Extra.forbid

    name: str
    started_at: Optional[Optional[datetime]] = None
    completed_at: Optional[Optional[datetime]] = None


class FreshnessThreshold(BaseParserModel):

    class Config:
        extra = Extra.forbid

    warn_after: Optional[Optional[Time]] = {'count': None, 'period': None}
    error_after: Optional[Optional[Time]] = {'count': None, 'period': None}
    filter: Optional[Optional[str]] = None


class SourceFreshnessOutput(BaseParserModel):

    class Config:
        extra = Extra.forbid

    unique_id: str
    max_loaded_at: datetime
    snapshotted_at: datetime
    max_loaded_at_time_ago_in_s: float
    status: Status1
    criteria: FreshnessThreshold
    adapter_response: Dict[str, Any]
    timing: List[TimingInfo]
    thread_id: str
    execution_time: float


class SourcesV3(BaseParserModel):

    class Config:
        extra = Extra.forbid

    metadata: FreshnessMetadata
    results: List[Union[SourceFreshnessRuntimeError, SourceFreshnessOutput]]
    elapsed_time: float
