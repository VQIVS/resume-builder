from pydantic import  BaseModel, Field 
from app.schemas.base import BaseDjangoModel

class UserCreateSchema(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    phone: str = Field(...)
    password: str


class UserResponse(BaseDjangoModel):
    name: str = Field(...)
    email: str = Field(...)
    phone: str = Field(...)
