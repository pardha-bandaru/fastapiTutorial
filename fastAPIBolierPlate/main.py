from fastapi import FastAPI
from fastAPIBolierPlate.apps.users.urls import userRouter

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI(
    title="FastAPI + Tortoise ORM + Sqlite with Django like(MVC) Boiler Plate",
    debug=True,
    description="Easy to use project structure for user shifting from Django to FastApi",
    docs_url="/docs",
)

models_list = [
    "fastAPIBolierPlate.apps.users.models",
]

all_routes = [
    {"route": userRouter, "prefix": "/users/v1"},
]

for route in all_routes:
    app.include_router(route["route"], prefix=route.get("prefix", ""))


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": models_list},
    generate_schemas=True,
    add_exception_handlers=True,
)
