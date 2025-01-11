from pydantic import Field
from app.schemas.base import BaseDjangoModel
from pydantic import BaseModel

class SectionCreateSchema(BaseModel):
    resume_id: int = Field(...)
    type: str = Field(...)
    order: int = Field(...)

class SectionResponse(BaseDjangoModel):
    section_id: int = Field(...)
    resume_id: int = Field(...)
    type: str = Field(...)
    order: int = Field(...)