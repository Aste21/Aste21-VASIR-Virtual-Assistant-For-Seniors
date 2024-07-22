from dataclasses import dataclass
from typing import List

DAYS_OF_THE_WEEK = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]


@dataclass
class Date:
    day_of_week: str
    hour: int
    minute: int


@dataclass
class Medicine:
    name: str
    when_to_take: List[Date]
    pills_count: float  # float because maybe sometimes half a pill should be taken
