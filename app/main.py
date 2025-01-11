import os
import django
from fastapi import FastAPI
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

app = FastAPI()

from app.api import resume, user, template, section, resume_template, content

# Include all routers with their respective paths
app.include_router(user.router, prefix="/user", tags=["Users"])
app.include_router(resume.router, prefix="/resume", tags=["Resume"])
app.include_router(template.router, prefix="/template", tags=["Template"])
app.include_router(section.router, prefix="/section", tags=["Section"])
app.include_router(resume_template.router, prefix="/resume-template", tags=["ResumeTemplate"])
app.include_router(content.router, prefix="/content", tags=["Content"])