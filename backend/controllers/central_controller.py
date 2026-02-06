from .user_controller import UserServices
from .task_controller import TaskService
from fastapi import APIRouter

router = APIRouter(
    tags=["Central Control"]
)

@router.post('/centralControl/create-user/')
async def create_user(data):
    return await UserServices.create_user(data)

@router.post('/centralControl/create-task/')
async def create_task(data):
    return await TaskService.createTask(data)