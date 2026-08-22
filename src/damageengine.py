"""
Quest 2: The Damage Engine (Dependency Inversion & Interfaces)

The Scenario:
You are building the core combat loop. A weapon needs to hit a target. 
However, the weapon shouldn't care if it is hitting a real Monster, a Training Barrel, or a destructible environment rock. 
It just needs to deal damage and lose sharpness.

The Raw JSON Input (Loadout Data):
JSON

{
  "weapon_name": "Wyvern Ignition",
  "weapon_class": "GreatSword",
  "raw_damage": 1056,
  "sharpness_units": 40
}

Your Mission:
Build a combat system using both abc and Protocol:

The Interface: 
    - Define a Protocol called DamageReceiver. 
    - Any object fulfilling this protocol must have a take_damage(amount: int) -> None method and an is_alive: bool property.

The Base Class: 
    - Create an abc.ABC called BaseMeleeWeapon. 
    - It must have a concrete method degrade_sharpness() that subtracts 1 from its sharpness, and an @abstractmethod called perform_attack(target: DamageReceiver).

The Concrete Classes: 
    - Create a GreatSword class that inherits from your ABC. 
    - Create a Monster dataclass that implicitly fulfills your DamageReceiver protocol (no inheritance!).

Function 1: equip_from_json(data: dict) -> BaseMeleeWeapon
- A factory function that reads the JSON and returns the instantiated weapon class.

Function 2: perform_attack(target: DamageReceiver) -> void
- (Implemented inside your GreatSword). It calculates damage, calls target.take_damage(), and calls self.degrade_sharpness().

Function 3: simulate_combat(weapon: BaseMeleeWeapon, target: DamageReceiver) -> void
- A standalone function that loops the attack until the target is no longer alive or the weapon breaks (sharpness hits 0).
"""

from typing import override
from typing import overload
from abc import ABC, abstractmethod
from typing import Protocol

class DamageReceiver(ABC):
    is_alive: bool

    @abstractmethod
    def take_damage(self, amount: int) -> None:
        ...


class Monster(DamageReceiver):
    def __init__(self, name: str) -> None:
        self._name: str = name

    @override
    def take_damage(self, amount: int) -> None:
        print(f"{self._name} has taken {amount} points of damage!")

monster = Monster("Chatacabra")
monster.take_damage(50)