from typing import List
from fastapi import APIRouter, HTTPException

from tortoise.contrib.fastapi import HTTPNotFoundError

from fastAPIBolierPlate.apps.users.models import Users
from fastAPIBolierPlate.apps.users.serializers import (
    Status,
    UserIn_Pydantic,
    User_Pydantic,
)


userRouter = APIRouter()


@userRouter.get("/users", response_model=List[User_Pydantic], tags=["Users"])
async def get_users():
    return await User_Pydantic.from_queryset(Users.all())


@userRouter.post("/users", response_model=User_Pydantic, tags=["Users"])
async def create_user(user: UserIn_Pydantic):
    user_obj = await Users.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@userRouter.get(
    "/user/{user_id}",
    response_model=User_Pydantic,
    responses={404: {"model": HTTPNotFoundError}},
    tags=["Users"],
)
async def get_user(user_id: int):
    return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


@userRouter.put(
    "/user/{user_id}",
    response_model=User_Pydantic,
    responses={404: {"model": HTTPNotFoundError}},
    tags=["Users"],
)
async def update_user(user_id: int, user: UserIn_Pydantic):
    await Users.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


@userRouter.delete(
    "/user/{user_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    tags=["Users"],
)
async def delete_user(user_id: int):
    deleted_count = await Users.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")
