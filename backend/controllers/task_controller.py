from fastapi import APIRouter
from services.task_services import TaskService

router = APIRouter(
    tags=["Tasks"]
)

@router.get('/tasks')
async def show_all_tasks():
    return await TaskService.read_all_task()

@router.get('/tasks/{id}')
async def show_task(taskId: int):
    return await TaskService.read_task_id(taskId)

@router.post('/tasks/create/{data}')
async def create_task(data):
    return await TaskService.createTask(data)