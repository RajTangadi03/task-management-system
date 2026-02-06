from fastapi import APIRouter, HTTPException, status
from services.user_services import UserServices
from schemas.user_schema import userData

router = APIRouter(
    tags=["Users"]
)

@router.get('/user/{id}')
async def userData(id: int):
    return await UserServices.read_user_id(id)

@router.get('/user')
async def show_all_user():
    return await UserServices.read_all_user()

@router.post('/user-reg')
async def create_user(data: userData):
    try:
        return await UserServices.create_user(data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

