from pydantic import Field
from app.schemas.base import BaseDjangoModel
from pydantic import BaseModel

class TemplateCreateSchema(BaseModel):
    name: str = Field(...)
    description: str = Field(...)

class TemplateResponse(BaseDjangoModel):
    template_id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)