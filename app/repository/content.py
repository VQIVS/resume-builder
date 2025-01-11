from typing import Optional
from app.models import Content
from django.shortcuts import get_object_or_404
from app.schemas.content import ContentResponse

async def create_new_content(**kwargs) -> ContentResponse:
    content = Content.objects.create(**kwargs)
    return ContentResponse.model_validate(content)

async def get_content_by_id(content_id: int) -> Optional[Content]:
    return get_object_or_404(Content, pk=content_id)

async def update_content_by_id(content_id: int, **kwargs) -> ContentResponse:
    content = get_object_or_404(Content, pk=content_id)
    for field, value in kwargs.items():
        setattr(content, field, value)
    content.save()
    return ContentResponse.model_validate(content)

async def delete_content_by_id(content_id: int) -> None:
    content = get_object_or_404(Content, pk=content_id)
    content.delete()
