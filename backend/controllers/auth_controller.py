from fastapi import APIRouter, Depends, HTTPException
from core import auth
from typing import Annotated

router = APIRouter()

# 1. Register the auth router
router.include_router(auth.router)

# 2. Define the User Dependency for protected routes
# This will now automatically handle the "Unauthorized" error if the token is missing/invalid
user_dependency = Annotated[dict, Depends(auth.get_current_user)]

@router.get("/", status_code=200)
async def get_user_details(user: user_dependency):
    # 'db' parameter is removed because your DAO handles connections.
    # 'auth.get_current_user' already raises an HTTPException if the token is invalid,
    # so 'user' will never be None here.
    return {"User": user}