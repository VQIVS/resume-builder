from typing import Optional
from app.models import ResumeToTemplate
from django.shortcuts import get_object_or_404
from asgiref.sync import sync_to_async

async def create_resume_template_mapping(resume_id: int, template_id: int) -> ResumeToTemplate:
    return await sync_to_async(ResumeToTemplate.objects.create)(
        resume_id_id=resume_id,
        template_id_id=template_id
    )

async def get_mapping_by_resume_id(resume_id: int) -> Optional[ResumeToTemplate]:
    return await sync_to_async(get_object_or_404)(ResumeToTemplate, resume_id=resume_id)

async def delete_mapping(mapping_id: int) -> None:
    mapping = await sync_to_async(get_object_or_404)(ResumeToTemplate, mapping_id=mapping_id)
    await sync_to_async(mapping.delete)()
