from fastapi import APIRouter, HTTPException, status
from services.user_services import userServices
from schemas.user_schema import userData

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/user-reg')
async def user_Reg(data: userData):
    try:
        return await userServices.create_user(data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

