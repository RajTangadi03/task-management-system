from fastapi import APIRouter
from services.task_services import TaskService
from schemas.task_schema import taskData

router = APIRouter(
    tags=["Tasks"]
)

@router.get('/tasks')
async def show_all_tasks():
    return await TaskService.read_all_task()

@router.get('/tasks/{id}')
async def show_task(taskId: int):
    return await TaskService.read_task_id(taskId)

async def create_task(data: taskData):
    return await TaskService.createTask(data)