from fastapi import FastAPI
from dao import database
from controllers import user_controller, task_controller, manager_controller, central_admin_controller, central_controller, auth_controller

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",  # React Vite frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect_db()

@app.on_event("shutdown")
async def shutdown():
    await database.close_db()

app.include_router(auth_controller.router)
app.include_router(central_admin_controller.router)
app.include_router(central_controller.router)
app.include_router(manager_controller.router)
app.include_router(task_controller.router)
app.include_router(user_controller.router)