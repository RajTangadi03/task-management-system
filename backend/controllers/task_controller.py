from fastapi import APIRouter
from services.task_services import TaskService
from schemas.task_schema import taskData, taskUpdateData

router = APIRouter(
    tags=["Tasks"]
)

@router.get('/tasks')
async def show_all_tasks():
    return await TaskService.read_all_task()

@router.get('/tasks/{id}')
async def show_task(taskId: int):
    return await TaskService.read_task_id(taskId)

@router.get('/tasks/users/{id}')
async def show_task_byuser(id: int):
    return await TaskService.read_taskByUser_id(id)

async def create_task(data: taskData):
    return await TaskService.createTask(data)

async def update_task(data: taskUpdateData, id: int):
    return await TaskService.updateTask(data, id)

async def delete_task(id: int):
    return await TaskService.deleteTask(id)