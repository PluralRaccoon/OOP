class Employee:
    employee_count = 0

    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position
        Employee.employee_count += 1

    def get_info(self):
        return f"{self.name} -> {self.position}"

    @staticmethod
    def is_valid_position(position: str):
        valid_positions: list[str] = ["manager", "cook", "janitor", "cashier"]
        return position.lower() in valid_positions

    @classmethod
    def get_employee_count(cls) -> int:
        return cls.employee_count