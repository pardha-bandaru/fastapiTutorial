from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from fastAPIBolierPlate.apps.users.models import Users


class Status(BaseModel):
    message: str


User_Pydantic = pydantic_model_creator(Users, name="User")

UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
