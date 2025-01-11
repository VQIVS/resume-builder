from fastapi import APIRouter, HTTPException
from app.models import Content
from app.schemas.content import ContentCreateSchema, ContentResponse
from app.repository.content import (
    create_new_content,
    get_content_by_id,
    update_content_by_id,
    delete_content_by_id,
)

router = APIRouter()

@router.post("/content")
async def create_content(content: ContentCreateSchema) -> ContentResponse:
    try:
        return await create_new_content(**content.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/content/{content_id}")
async def get_content(content_id: int) -> ContentResponse:
    try:
        content_obj: Content = await get_content_by_id(content_id)
        return ContentResponse.model_validate(content_obj)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/content/{content_id}")
async def update_content(content_id: int, content: ContentCreateSchema) -> ContentResponse:
    try:
        return await update_content_by_id(content_id, **content.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/content/{content_id}")
async def delete_content(content_id: int):
    try:
        await delete_content_by_id(content_id)
        return {"detail": "Content deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
