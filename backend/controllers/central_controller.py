from fastapi import APIRouter, Depends, HTTPException, status
from .user_controller import UserServices
from .task_controller import TaskService
from schemas.task_schema import taskData, taskUpdateData
from schemas.user_schema import userData
from core.auth import get_current_user
from typing import Annotated

router = APIRouter(
    tags=["Central Control"]
)

@router.post('/centralControl/create-user/')
async def create_user(data: userData):
    # if current_user["role"] != "admin":
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admins only")
    
    return await UserServices.create_user(data)

@router.post('/centralControl/create-task/')
async def create_task(data: taskData, current_user: Annotated[dict, Depends(get_current_user)]):
    if current_user["role"] not in ["admin", "manager"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Insufficient permissions")

    return await TaskService.createTask(data)

@router.put('/centralControl/update-task/{id}')
async def update_task(data: taskUpdateData, id: int, current_user: Annotated[dict, Depends(get_current_user)]):
    if current_user["role"] not in ["admin", "manager", "user"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Insufficient permissions")
    
    return await TaskService.updateTask(data, id)

@router.delete('/centralControl/delete-task/{id}')
async def delete_task(id: int, current_user: Annotated[dict, Depends(get_current_user)]):
    if current_user["role"] not in ["admin", "manager"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Insufficient permissions")
    
    return await TaskService.deleteTask(id)

@router.put('/centralControl/update-user/{id}')
async def update_user(data: userData, id: int, current_user: Annotated[dict, Depends(get_current_user)]):
    if current_user["role"] not in ["admin", "manager"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Insufficient permissions")
    
    return await UserServices.update_user(data, id)

@router.delete('/centralControl/delete-user/{id}')
async def delete_user(id: int, current_user: Annotated[dict, Depends(get_current_user)]):
    if current_user["role"] not in ["admin", "manager"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Insufficient permissions")
    
    return await UserServices.delete_user(id)

@router.get('/centralControl/get-user-tasks/{id}')
async def show_task(taskId: int):
    return await TaskService.read_task_id(taskId)