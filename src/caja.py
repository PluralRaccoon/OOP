class Employee:

    def __init__(self, name: str, base_salary: float, performance_multiplier: float):
        self._name = name
        self._base_salary = base_salary
        # This automatically routes through your @performance_multiplier.setter!
        self.performance_multiplier = performance_multiplier

    @classmethod
    def from_dict(cls, data: dict):
        return Employee(**data)

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
    def performance_multiplier(self, new_multiplier: float):
        if 1.0 <= new_multiplier <= 1.5:
            raise ValueError("New multiplier must be greater or equal to 1.0 and less than or equal to 1.5")
        self._performance_multiplier = new_multiplier

    @property
    def bonus(self):
        return self._base_salary * self._performance_multiplier


test = {
    "name": "Charlie",
    "base_salary": 2176300,
    "performance_multiplier": 1.5
}

charlie = Employee.from_dict(test)

print(charlie.name)

bob = Employee("Bob", 100, 1.25)
print(bob.name) # Works! Returns "Bob"
bob.name = "Alice" # Fails! Raises AttributeError (Immutability achieved)

bob.performance_multiplier = 1.35 # Works! Passes through the setter validation
bob.performance_multiplier = 0.5 # Fails! Raises ValueError
