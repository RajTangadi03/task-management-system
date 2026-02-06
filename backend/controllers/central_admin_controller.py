from fastapi import APIRouter
from .manager_controller import MangerService

router = APIRouter(
    tags=["Admin"]
)

@router.post('/admin/create-manager/')
async def create_manager(data):
    return await MangerService.create_manager(data)