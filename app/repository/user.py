from app.models import User
from asgiref.sync import sync_to_async

async def create_new_user(name: str, email: str, password: str, phone: str) -> User:
    return await sync_to_async(User.objects.create)(
        name=name,
        email=email,
        password=password,
        phone=phone
    )

async def get_user_by_id(user_id: int) -> User:
    return await sync_to_async(User.objects.get)(user_id=user_id)
