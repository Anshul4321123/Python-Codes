# Basic Field Types and Default Values

from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int
    alive: bool


u = Person(name="John",age=30, alive=True)
print(u)

# Custom Validation Rules with Pydantic

from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    age: int = Field(..., gt=0, lt=120)
    email: str = Field(..., regex=r'^\S+@\S+\.\S+$')

# Advanced: Custom Validators

from pydantic import BaseModel, validator, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    age: int

    @validator("username")
    def no_spaces(cls, v):
        if " " in v:
            raise ValueError("Username must not contain spaces")
        return v

    @validator("age")
    def age_must_be_realistic(cls, v):
        if v < 13:
            raise ValueError("User must be at least 13 years old")
        return v

