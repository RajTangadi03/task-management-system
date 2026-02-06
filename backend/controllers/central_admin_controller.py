from fastapi import APIRouter
from .manager_controller import MangerService
from schemas.manager_schema import managerData

router = APIRouter(
    tags=["Admin"]
)

@router.post('/admin/create-manager/')
async def create_manager(data: managerData):
    return await MangerService.create_manager(data)

@router.put('/admin/update-manager/{id}')
async def update_manager(data: managerData, id: int):
    return await MangerService.update_manager(data, id)

@router.delete('/admin/delete-manager/{id}')
async def delete_manager(id: int):
    return await MangerService.delete_manager(id)