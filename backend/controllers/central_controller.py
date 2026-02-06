from .user_controller import UserServices
from .task_controller import TaskService
from fastapi import APIRouter
from schemas.task_schema import taskData, taskUpdateData
from schemas.user_schema import userData

router = APIRouter(
    tags=["Central Control"]
)

@router.post('/centralControl/create-user/')
async def create_user(data: userData):
    return await UserServices.create_user(data)

@router.post('/centralControl/create-task/')
async def create_task(data: taskData):
    return await TaskService.createTask(data)

@router.put('/centralControl/update-task/{id}')
async def update_task(data: taskUpdateData, id: int):
    return await TaskService.updateTask(data, id)

@router.delete('/centralControl/delete-task/{id}')
async def delete_task(id: int):
    return await TaskService.deleteTask(id)

@router.put('/centralControl/update-user/{id}')
async def update_user(data: userData, id: int):
    return await UserServices.update_user(data, id)

@router.delete('/centralControl/delete-user/{id}')
async def delete_user(id: int):
    return await UserServices.delete_user(id)