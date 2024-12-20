from dataclasses import dataclass
from datetime import datetime


@dataclass
class HealthResponse:
    status: str
    datetime: datetime
