from pydantic import BaseModel

class ResumeTemplateBase(BaseModel):
    resume_id: int
    template_id: int

class ResumeTemplateCreate(ResumeTemplateBase):
    pass

class ResumeTemplateResponse(ResumeTemplateBase):
    id: int
    
    class Config:
        from_attributes = True
