from fastapi import APIRouter
from services.user_services import userServices

router = APIRouter()

@router.get('/user/{id}')
async def userData(id: int):
    return await userServices.read_user_id(id)