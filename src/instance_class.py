from unittest import case


class Hunter:
    __slots__ = ["_name", "_level", "_rank", "_flag"]

    def __init__(self, name: str, rank: int, level: str):
        self._name = name
        self._rank = rank
        self._level = level

    @property
    def name(self) -> str:
        return self._name

    @property
    def flag(self):
        match self._level.upper():
            case "LOW":
                return "Low Rank"
            case "HIGH":
                return "High Rank"
            case "MASTER":
                return "Master Rank"
            case _:
                return "Unknown"

from typing import final

racun = Hunter("Racun", 300, "Master")

print(racun.name)
print(f"Cazador {racun.name} de rango: {racun._rank} -> {racun.flag}")