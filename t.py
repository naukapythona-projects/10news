# Why dataclasses?
from __future__ import annotations
from datetime import date
from dataclasses import dataclass, field

@dataclass(order=True)
class Person:
    name: str = field(compare=False)
    surname: str
    birth_date: date = field(compare=False)

print(Person("John", "Doe", date.today()))