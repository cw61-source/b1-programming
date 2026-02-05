from pydantic import BaseModel

# Base model for creating users
class UserCreate(BaseModel):
    name: str
    email: str
    age: int

# Full user model with ID
class User(UserCreate):
    id: int