from dataclasses import dataclass
from typing import Optional


@dataclass
class Employee:
    id: int
    username: str
    first_name: str
    last_name: Optional[str] = None
    patronymic: Optional[str] = None
