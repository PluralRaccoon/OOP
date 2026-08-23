from pydantic import BaseModel, field_validator

"""--- Pydantic - Basic Validators ---"""

# Why validate?
# Setting up a validator to check a field
# Modifying values
# Reusing validators

class Person(BaseModel):
    """A class represent a Person"""
    name: str
    age: int

    @field_validator("name")
    def check_name_is_alpha(word: str) -> str:
        if not word.isalpha():
            raise ValueError(f"{word} isn't correctly formed!")
        return word

    @field_validator("age")
    def check_correct_age(age: int) -> int:
        if age < 1 or age > 100:
            raise ValueError(f"{age} isn't correctly formed!")
        return age

def main() -> None:
    charlie = Person(name="Charlie", age=29)
    print(charlie)

if __name__ == "__main__":
    main()