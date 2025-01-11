from typing import Self
from django.forms import model_to_dict
from pydantic import BaseModel, model_validator


class BaseDjangoModel(BaseModel):
    @model_validator(mode='before')
    def django_serialize(self) -> Self:
        return model_to_dict(self)