from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserCreate, UserLogin
from app.services.auth import create_user, authenticate_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=dict)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    return await create_user(db, user)

@router.post("/login", response_model=dict)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    return authenticate_user(db, user)