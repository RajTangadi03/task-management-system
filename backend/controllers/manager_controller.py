from fastapi import APIRouter
from services.manager_services import MangerService
from schemas.manager_schema import managerData

router = APIRouter(
    tags=["Manager"]
)

@router.get('/manager')
async def show_all_manager():
    return await MangerService.read_all_manager()

@router.get('/manager/{id}')
async def show_manager(managerId: int):
    return await MangerService.read_manager_id(managerId)

async def create_manager(data: managerData):
    return await MangerService.create_manager(data)

async def update_manager(data: managerData, id: int):
    return await MangerService.update_manager(data, id)

async def delete_manager(id: int):
    return await MangerService.delete_manager(id)