from typing import Optional
from app.models import Template
from django.shortcuts import get_object_or_404
from app.schemas.template import TemplateResponse

async def create_new_template(**kwargs) -> TemplateResponse:
    template = Template.objects.create(**kwargs)
    return TemplateResponse.model_validate(template)

async def get_template_by_id(template_id: int) -> Optional[Template]:
    return get_object_or_404(Template, pk=template_id)

async def update_template_by_id(template_id: int, **kwargs) -> TemplateResponse:
    template = get_object_or_404(Template, pk=template_id)
    for field, value in kwargs.items():
        setattr(template, field, value)
    template.save()
    return TemplateResponse.model_validate(template)

async def delete_template_by_id(template_id: int) -> None:
    template = get_object_or_404(Template, pk=template_id)
    template.delete()
