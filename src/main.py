from pydantic import BaseModel
from typing import Optional

# Default: if not passed in, set to some value
# Optional: Effectively the same as default, but we can pass None!
class User(BaseModel):
    """A class to represent a simple user.

    Args:
        user (str): name of the user
        age (int): age of the user
    """
    name: str
    age: int
    pass_induction: bool
    # years_experience: int = 0
    # years_experience: Optional[int] = 0
    years_experience: int | float | str
    awards: list[str]

class ServerConfig(BaseModel):
    hostname: str
    ram_gb: int
    is_active: bool


def main() -> None:
    user = User(
        name="Charlie", 
        age="29", 
        pass_induction=True, 
        years_experience="1 week", 
        awards=["AWS Cert", "Terraform Cert"]
    )

    # print(user)

    server1 = ServerConfig(
        hostname="db-prod-01",
        ram_gb=64,
        is_active=True
    )

    print(server1.ram_gb) # I can use dot notation to access my model's fields

    # Coercion (Parsing in action)
    raw_data: dict[str, str] = {"hostname": "cache-01", "ram_gb": "32", "is_active": "true"}
    server2 = ServerConfig(**raw_data)

    # Pydantic coerced the strings into the correct Python types
    print(repr(server2.ram_gb))
    print(repr(server2.is_active))

if __name__ == "__main__":
    main()