from sqlalchemy.orm import Session
from app.models import ProviderProfile
from app.schemas import ProviderProfileCreate

def get_providers(db: Session):
    return db.query(ProviderProfile).all()

def get_provider(db: Session, provider_id: int):
    return db.query(ProviderProfile).filter(ProviderProfile.id == provider_id).first()

def create_provider_profile(db: Session, profile: ProviderProfileCreate, user_id: int):
    db_profile = ProviderProfile(
        user_id=user_id,
        category=profile.category,
        description=profile.description,
        hourly_rate=profile.hourly_rate
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile