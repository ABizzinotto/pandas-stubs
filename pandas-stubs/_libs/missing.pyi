from __future__ import annotations

class NAType:
    def __new__(cls, *args, **kwargs) -> NAType: ...
    def __format__(self, format_spec: str) -> str: ...
    def __bool__(self) -> None: ...
    def __hash__(self) -> int: ...
    def __reduce__(self) -> str: ...
    def __add__(self, other) -> NAType: ...
    def __radd__(self, other) -> NAType: ...
    def __sub__(self, other) -> NAType: ...
    def __rsub__(self, other) -> NAType: ...
    def __mul__(self, other) -> NAType: ...
    def __rmul__(self, other) -> NAType: ...
    def __matmul__(self, other) -> NAType: ...
    def __rmatmul__(self, other) -> NAType: ...
    def __truediv__(self, other) -> NAType: ...
    def __rtruediv__(self, other) -> NAType: ...
    def __floordiv__(self, other) -> NAType: ...
    def __rfloordiv__(self, other) -> NAType: ...
    def __mod__(self, other) -> NAType: ...
    def __rmod__(self, other) -> NAType: ...
    def __divmod__(self, other) -> NAType: ...
    def __rdivmod__(self, other) -> NAType: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __neg__(self, other) -> NAType: ...
    def __pos__(self, other) -> NAType: ...
    def __abs__(self, other) -> NAType: ...
    def __invert__(self, other) -> NAType: ...
    def __pow__(self, other) -> NAType: ...
    def __rpow__(self, other) -> NAType: ...
    def __and__(self, other) -> NAType | None: ...
    __rand__ = __and__
    def __or__(self, other) -> bool | NAType: ...
    __ror__ = __or__
    def __xor__(self, other) -> NAType: ...
    __rxor__ = __xor__
    __array_priority__: int
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs): ...

NA: NAType = ...
