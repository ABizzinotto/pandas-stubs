from __future__ import annotations

from datetime import timedelta
from typing import Sequence

from pandas.core.arrays import datetimelike as dtl

class TimedeltaArray(dtl.DatetimeLikeArrayMixin, dtl.TimelikeOps):
    __array_priority__: int = ...
    @property
    def dtype(self): ...
    def __init__(self, values, dtype=..., freq=..., copy: bool = ...) -> None: ...
    def astype(self, dtype, copy: bool = ...): ...
    def sum(
        self,
        axis=...,
        dtype=...,
        out=...,
        keepdims: bool = ...,
        initial=...,
        skipna: bool = ...,
        min_count: int = ...,
    ): ...
    def std(
        self,
        axis=...,
        dtype=...,
        out=...,
        ddof: int = ...,
        keepdims: bool = ...,
        skipna: bool = ...,
    ): ...
    def median(
        self,
        axis=...,
        out=...,
        overwrite_input: bool = ...,
        keepdims: bool = ...,
        skipna: bool = ...,
    ): ...
    def __mul__(self, other): ...
    __rmul__ = ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def __floordiv__(self, other): ...
    def __rfloordiv__(self, other): ...
    def __mod__(self, other): ...
    def __rmod__(self, other): ...
    def __divmod__(self, other): ...
    def __rdivmod__(self, other): ...
    def __neg__(self): ...
    def __pos__(self): ...
    def __abs__(self): ...
    def total_seconds(self) -> int: ...
    def to_pytimedelta(self) -> Sequence[timedelta]: ...
    days: int = ...
    seconds: int = ...
    microseconds: int = ...
    nanoseconds: int = ...
    @property
    def components(self) -> int: ...

def sequence_to_td64ns(data, copy: bool = ..., unit: str = ..., errors: str = ...): ...
def ints_to_td64ns(data, unit: str = ...): ...
def objects_to_td64ns(data, unit: str = ..., errors: str = ...): ...
