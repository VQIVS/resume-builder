from pydantic import Field
from app.schemas.base import BaseDjangoModel
from pydantic import BaseModel

class ContentCreateSchema(BaseModel):
    section_id: int = Field(...)
    field_name: str = Field(...)
    value: str = Field(...)

class ContentResponse(BaseDjangoModel):
    content_id: int = Field(...)
    section_id: int = Field(...)
    field_name: str = Field(...)
    value: str = Field(...)