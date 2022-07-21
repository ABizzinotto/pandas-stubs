from __future__ import annotations

from typing import Callable

class CachedProperty:
    def __init__(self, func: Callable) -> None: ...
    def __get__(self, obj, typ): ...
    def __set__(self, obj, value) -> None: ...

cache_readonly: CachedProperty = ...

class AxisProperty:
    def __init__(self, axis: int = ..., doc: str = ...) -> None: ...
    def __get__(self, obj, typ): ...
    def __set__(self, obj, value) -> None: ...
