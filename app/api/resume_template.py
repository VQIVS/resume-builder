from fastapi import APIRouter, HTTPException
from app.repository.resume_template import (
    create_resume_template_mapping,
    get_mapping_by_resume_id,
    delete_mapping
)
from app.schemas.resume_template import ResumeTemplateCreate, ResumeTemplateResponse

router = APIRouter()

@router.post("/resume-template")
async def create_mapping(mapping: ResumeTemplateCreate) -> ResumeTemplateResponse:
    try:
        result = await create_resume_template_mapping(
            mapping.resume_id,
            mapping.template_id
        )
        return ResumeTemplateResponse.model_validate(result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/resume-template/{resume_id}")
async def get_template_for_resume(resume_id: int) -> ResumeTemplateResponse:
    try:
        result = await get_mapping_by_resume_id(resume_id)
        return ResumeTemplateResponse.model_validate(result)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Mapping not found")

@router.delete("/resume-template/{mapping_id}")
async def delete_template_mapping(mapping_id: int):
    try:
        await delete_mapping(mapping_id)
        return {"detail": "Mapping deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
