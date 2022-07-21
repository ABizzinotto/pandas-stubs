from __future__ import annotations

from typing import Sequence

import numpy as np
from pandas.core.arrays.base import (
    ExtensionArray as ExtensionArray,
    ExtensionOpsMixin as ExtensionOpsMixin,
)

from pandas._libs import (
    NaT as NaT,
    NaTType as NaTType,
    Timestamp as Timestamp,
)

class AttributesMixin: ...

class DatelikeOps:
    def strftime(self, date_format): ...

class TimelikeOps:
    def round(self, freq, ambiguous: str = ..., nonexistent: str = ...): ...
    def floor(self, freq, ambiguous: str = ..., nonexistent: str = ...): ...
    def ceil(self, freq, ambiguous: str = ..., nonexistent: str = ...): ...

class DatetimeLikeArrayMixin(ExtensionOpsMixin, AttributesMixin, ExtensionArray):
    @property
    def ndim(self) -> int: ...
    @property
    def shape(self): ...
    def reshape(self, *args, **kwargs): ...
    def ravel(self, *args, **kwargs): ...
    def __iter__(self): ...
    @property
    def asi8(self) -> np.ndarray: ...
    @property
    def nbytes(self): ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    @property
    def size(self) -> int: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key: int | Sequence[int] | Sequence[bool] | slice, value) -> None: ...  # type: ignore[override]
    def astype(self, dtype, copy: bool = ...): ...
    def view(self, dtype=...): ...
    def unique(self): ...
    def take(self, indices, allow_fill: bool = ..., fill_value=...): ...
    def copy(self): ...
    def shift(self, periods: int = ..., fill_value=..., axis: int = ...): ...
    def searchsorted(self, value, side: str = ..., sorter=...): ...
    def repeat(self, repeats, *args, **kwargs): ...
    def value_counts(self, dropna: bool = ...): ...
    def map(self, mapper): ...
    def isna(self): ...
    def fillna(self, value=..., method=..., limit=...): ...
    @property
    def freq(self): ...
    @freq.setter
    def freq(self, value) -> None: ...
    @property
    def freqstr(self): ...
    @property
    def inferred_freq(self): ...
    @property
    def resolution(self): ...
    __pow__ = ...
    __rpow__ = ...
    __mul__ = ...
    __rmul__ = ...
    __truediv__ = ...
    __rtruediv__ = ...
    __floordiv__ = ...
    __rfloordiv__ = ...
    __mod__ = ...
    __rmod__ = ...
    __divmod__ = ...
    __rdivmod__ = ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __iadd__(self, other): ...
    def __isub__(self, other): ...
    def min(self, axis=..., skipna: bool = ..., *args, **kwargs): ...
    def max(self, axis=..., skipna: bool = ..., *args, **kwargs): ...
    def mean(self, skipna: bool = ...): ...

def validate_periods(periods): ...
def validate_endpoints(closed): ...
def validate_inferred_freq(freq, inferred_freq, freq_infer): ...
def maybe_infer_freq(freq): ...
