from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.core.security import get_current_user
from app.schemas import ProviderProfile, ProviderProfileCreate
from app.services.providers import get_providers, get_provider, create_provider_profile

router = APIRouter(prefix="/providers", tags=["providers"])

@router.get("/", response_model=List[ProviderProfile])
async def list_providers(db: Session = Depends(get_db)):
    return get_providers(db)

@router.get("/{provider_id}", response_model=ProviderProfile)
async def get_provider_details(provider_id: int, db: Session = Depends(get_db)):
    provider = get_provider(db, provider_id)
    if not provider:
        raise HTTPException(status_code=404, detail="Provider not found")
    return provider

@router.post("/", response_model=ProviderProfile)
async def create_profile(
    profile: ProviderProfileCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_provider_profile(db, profile, current_user.id)