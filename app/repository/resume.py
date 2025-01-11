from app.models import Resume
from asgiref.sync import sync_to_async


async def create_resume(user_id: int, title: str) -> Resume:
    return await sync_to_async(Resume.objects.create)(user_id=user_id, title=title)


async def get_resume_by_id(resume_id: int) -> Resume:
    return await sync_to_async(Resume.objects.get)(resume_id=resume_id)

async def update_resume(resume_id: int, title: str) -> Resume:
    resume = await sync_to_async(Resume.objects.get)(id=resume_id)
    resume.title = title
    await sync_to_async(resume.save)()
    return resume

async def delete_resume(resume_id: int) -> None:
    resume = await sync_to_async(Resume.objects.get)(id=resume_id)
    await sync_to_async(resume.delete)()
