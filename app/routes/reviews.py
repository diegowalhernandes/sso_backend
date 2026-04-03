from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.core.security import get_current_user
from app.schemas import Review, ReviewCreate
from app.services.reviews import create_review, get_reviews_for_provider

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.post("/", response_model=Review)
async def add_review(
    review: ReviewCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_review(db, review, current_user.id)

@router.get("/providers/{provider_id}", response_model=List[Review])
async def get_provider_reviews(provider_id: int, db: Session = Depends(get_db)):
    return get_reviews_for_provider(db, provider_id)