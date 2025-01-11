from fastapi import APIRouter, HTTPException
from app.models import Template
from app.schemas.template import TemplateCreateSchema, TemplateResponse
from app.repository.template import (
    create_new_template,
    get_template_by_id,
    update_template_by_id,
    delete_template_by_id,
)

router = APIRouter()

@router.post("/template")
async def create_template(template: TemplateCreateSchema) -> TemplateResponse:
    try:
        return await create_new_template(**template.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/template/{template_id}")
async def get_template(template_id: int) -> TemplateResponse:
    try:
        template: Template = await get_template_by_id(template_id)
        return TemplateResponse.model_validate(template)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/template/{template_id}")
async def update_template(template_id: int, template: TemplateCreateSchema) -> TemplateResponse:
    try:
        return await update_template_by_id(template_id, **template.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/template/{template_id}")
async def delete_template(template_id: int):
    try:
        await delete_template_by_id(template_id)
        return {"detail": "Template deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
