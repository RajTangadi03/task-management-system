from fastapi import APIRouter
from services.user_services import userServices
from schemas.user_schema import user

router = APIRouter()

@router.post('/user-reg')
async def userData(data: user):
    return await userServices.create_user(data)