from __future__ import annotations

import numpy as np
from pandas.core import accessor
from pandas.core.indexes.base import Index  # , maybe_extract_name
from pandas.core.indexes.extension import ExtensionIndex

from pandas._typing import DtypeArg

class CategoricalIndex(ExtensionIndex, accessor.PandasDelegate):
    codes: np.ndarray = ...
    categories: Index = ...
    def __new__(
        cls,
        data=...,
        categories=...,
        ordered=...,
        dtype=...,
        copy: bool = ...,
        name=...,
    ) -> CategoricalIndex: ...
    def equals(self, other): ...
    @property
    def inferred_type(self) -> str: ...
    @property
    def values(self): ...
    def __contains__(self, key) -> bool: ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def astype(self, dtype: DtypeArg, copy: bool = ...) -> Index: ...
    def fillna(self, value, downcast=...): ...
    def is_unique(self) -> bool: ...
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    def unique(self, level=...): ...
    def duplicated(self, keep: str = ...): ...
    def get_loc(self, key, method=...): ...
    def get_value(self, seriesArrayLike, key): ...
    def where(self, cond, other=...): ...
    def reindex(self, target, method=..., level=..., limit=..., tolerance=...): ...
    def get_indexer(self, target, method=..., limit=..., tolerance=...): ...
    def get_indexer_non_unique(self, target): ...
    def take_nd(self, *args, **kwargs): ...
    def map(self, mapper): ...
    def delete(self, loc): ...
    def insert(self, loc, item): ...
