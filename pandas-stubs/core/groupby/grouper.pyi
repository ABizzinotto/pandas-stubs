from __future__ import annotations

from typing import Hashable

import numpy as np
from pandas.core.groupby.ops import BaseGrouper
from pandas.core.indexes.api import Index

from pandas._typing import (
    FrameOrSeries,
    FrameOrSeriesUnion,
)

class Grouper:
    def __new__(cls, *args, **kwargs): ...
    key = ...
    level = ...
    freq = ...
    axis = ...
    sort = ...
    grouper = ...
    obj = ...
    indexer = ...
    binner = ...
    def __init__(
        self, key=..., level=..., freq=..., axis: int = ..., sort: bool = ...
    ) -> None: ...
    @property
    def ax(self): ...
    @property
    def groups(self): ...

class Grouping:
    name = ...
    level = ...
    grouper = ...
    all_grouper = ...
    index = ...
    sort = ...
    obj = ...
    observed = ...
    in_axis = ...
    def __init__(
        self,
        index: Index,
        grouper=...,
        obj: FrameOrSeriesUnion | None = ...,
        name=...,
        level=...,
        sort: bool = ...,
        observed: bool = ...,
        in_axis: bool = ...,
    ) -> None: ...
    def __iter__(self): ...
    @property
    def ngroups(self) -> int: ...
    def indices(self): ...
    @property
    def codes(self) -> np.ndarray: ...
    def result_index(self) -> Index: ...
    @property
    def group_index(self) -> Index: ...
    def groups(self) -> dict[Hashable, np.ndarray]: ...

def get_grouper(
    obj: FrameOrSeries,
    key=...,
    axis: int = ...,
    level=...,
    sort: bool = ...,
    observed: bool = ...,
    mutated: bool = ...,
    validate: bool = ...,
) -> tuple[BaseGrouper, list[Hashable], FrameOrSeries]: ...
