from fastapi import APIRouter, HTTPException

from app.models import Resume, User
from app.repository.user import create_new_user, get_user_by_id
from app.schemas.user import UserCreateSchema, UserResponse

router = APIRouter()


@router.post("/user")
async def create_user(user : UserCreateSchema) -> UserResponse:
    try:
        return await create_new_user(**user.model_dump())

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/user/{user_id}")
async def get_user(user_id: int) -> UserResponse:
    try:
        user: User = await get_user_by_id(user_id)
        return UserResponse.model_validate(user)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
