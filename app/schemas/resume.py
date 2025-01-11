from app.schemas.base import BaseDjangoModel
from pydantic import BaseModel

class ResumeCreateSchema(BaseModel):
    title: str
    user_id: int
    
class ResumeResponse(BaseDjangoModel):
    id : int
    user_id: int
    title: str

class ResumeUpdateSchema(BaseModel):
    title: str
