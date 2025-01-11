from fastapi import APIRouter, HTTPException

from app.models import Resume
from app.repository.resume import create_resume, get_resume_by_id, update_resume, delete_resume
from app.schemas.resume import ResumeCreateSchema, ResumeResponse, ResumeUpdateSchema

router = APIRouter()


@router.post("/resume")
async def create_new_resume(resume: ResumeCreateSchema) -> ResumeResponse:
    try:
        return await create_resume(resume.user_id, resume.title)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/resume/{resume_id}")
async def get_resume(resume_id: int) -> ResumeResponse:
    try:
        resume: Resume = await get_resume_by_id(resume_id)
        return ResumeResponse.model_validate(resume)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/resume/{resume_id}")
async def update_existing_resume(resume_id: int, resume: ResumeUpdateSchema) -> ResumeResponse:
    try:
        updated_resume: Resume = await update_resume(resume_id, resume.title)
        return ResumeResponse.model_validate(updated_resume)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/resume/{resume_id}")
async def delete_existing_resume(resume_id: int) -> None:
    try:
        await delete_resume(resume_id)
        return {"detail": "Resume deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
