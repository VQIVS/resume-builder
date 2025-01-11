from typing import Optional
from app.models import Section
from django.shortcuts import get_object_or_404
from app.schemas.section import SectionResponse

async def create_new_section(**kwargs) -> SectionResponse:
    section = Section.objects.create(**kwargs)
    return SectionResponse.model_validate(section)

async def get_section_by_id(section_id: int) -> Optional[Section]:
    return get_object_or_404(Section, pk=section_id)

async def update_section_by_id(section_id: int, **kwargs) -> SectionResponse:
    section = get_object_or_404(Section, pk=section_id)
    for field, value in kwargs.items():
        setattr(section, field, value)
    section.save()
    return SectionResponse.model_validate(section)

async def delete_section_by_id(section_id: int) -> None:
    section = get_object_or_404(Section, pk=section_id)
    section.delete()
