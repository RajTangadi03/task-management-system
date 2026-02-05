from fastapi import FastAPI
from dao.database import db
from .controllers import user_controller, user_registration_controller

app = FastAPI()

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

app.include_router(user_controller.router)
app.include_router(user_registration_controller.router)