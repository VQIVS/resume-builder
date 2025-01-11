from fastapi import APIRouter, HTTPException
from app.models import Section
from app.schemas.section import SectionCreateSchema, SectionResponse
from app.repository.section import (
    create_new_section,
    get_section_by_id,
    update_section_by_id,
    delete_section_by_id,
)

router = APIRouter()

@router.post("/section")
async def create_section(section: SectionCreateSchema) -> SectionResponse:
    try:
        return await create_new_section(**section.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/section/{section_id}")
async def get_section(section_id: int) -> SectionResponse:
    try:
        section_obj: Section = await get_section_by_id(section_id)
        return SectionResponse.model_validate(section_obj)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/section/{section_id}")
async def update_section(section_id: int, section: SectionCreateSchema) -> SectionResponse:
    try:
        return await update_section_by_id(section_id, **section.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/section/{section_id}")
async def delete_section(section_id: int):
    try:
        await delete_section_by_id(section_id)
        return {"detail": "Section deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
