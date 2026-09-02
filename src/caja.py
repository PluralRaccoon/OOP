from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import override, Any
from pydantic import BaseModel, field_validator

@dataclass(frozen=True)
class BankAccount(BaseModel):
    bank_name: str
    account_number: str

class Worker(ABC):
    @property
    @abstractmethod
    def name(self):
        ...

    @property
    @abstractmethod
    def total_pay(self):
        ...

    @property
    @abstractmethod
    def routing_instructions(self):
        ...


class Employee(BaseModel, Worker):

    def __init__(self, name: str, base_salary: float, performance_multiplier: float, bank_account: BankAccount):
        self._name = name
        self._base_salary = base_salary
        # This automatically routes through your @performance_multiplier.setter!
        self.performance_multiplier = performance_multiplier
        self._bank_account = bank_account

    @classmethod
    def from_dict(cls, data: dict):
        return Employee(data["name"], data["base_salary"], data["performance_multiplier"], BankAccount.from_dict(data["bank_account"]))

    @override
    @property
    def name(self):
        return self._name

    @property
    def base_salary(self):
        return self._base_salary

    @property
    def performance_multiplier(self):
        return self._performance_multiplier

    @performance_multiplier.setter
    def performance_multiplier(self, new_multiplier: float| int):
        if new_multiplier < 1.0 or new_multiplier > 1.5:
            raise ValueError("Performance multiplier must be between 1.0 and 1.5")
        self._performance_multiplier = new_multiplier

    @property
    def bonus(self) -> float | int:
        return self._base_salary * self._performance_multiplier

    @override
    @property
    def total_pay(self) -> float:
        return self.bonus + self.base_salary

    @override
    @property
    def routing_instructions(self) -> str:
        return f"Bank: {self._bank_account.bank_name}, Account: {self._bank_account.account_number}"

class Contractor(BaseModel, Worker):
    def __init__(self, name: str, hourly_rate: float, hours_worked: int, bank_account: BankAccount):
        self._name = name
        self._hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self._bank_account = bank_account

    @override
    @property
    def name(self):
        return self._name

    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, new_hours_worked: int):
        if new_hours_worked < 20 or new_hours_worked > 48:
            raise ValueError("Hours worked must be between 20 and 48 tops by law.")
        self._hours_worked = new_hours_worked

    @override
    @property
    def total_pay(self):
        return self._hourly_rate * self._hours_worked

    @override
    @property
    def routing_instructions(self) -> str:
        return f"Bank: {self._bank_account.bank_name}, Account: {self._bank_account.account_number}"


raw_payload: dict[str, Any] = {
    "name": "Alice",
    "base_salary": 120000,
    "performance_multiplier": 1.2,
    "bank_account": {
        "bank_name": "Bank of America",
        "account_number": "123456789"
    }
}

# print(raw_payload.get("bank_account"))

alice = Employee.from_dict(raw_payload)

print(alice.routing_instructions)