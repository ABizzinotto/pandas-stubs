from __future__ import annotations

from datetime import datetime

def localize_pydatetime(dt: datetime, tz: object) -> datetime: ...

class OutOfBoundsTimedelta(ValueError): ...
