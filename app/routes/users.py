from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.schemas import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=User)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    return current_user