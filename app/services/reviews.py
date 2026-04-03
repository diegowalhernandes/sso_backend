from sqlalchemy.orm import Session
from app.models import Review
from app.schemas import ReviewCreate

def create_review(db: Session, review: ReviewCreate, client_id: int):
    db_review = Review(
        client_id=client_id,
        provider_id=review.provider_id,
        rating=review.rating,
        comment=review.comment
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    # Update provider rating
    provider = db.query(ProviderProfile).filter(ProviderProfile.user_id == review.provider_id).first()
    if provider:
        reviews = db.query(Review).filter(Review.provider_id == review.provider_id).all()
        avg_rating = sum(r.rating for r in reviews) / len(reviews)
        provider.rating = avg_rating
        db.commit()
    return db_review

def get_reviews_for_provider(db: Session, provider_id: int):
    return db.query(Review).filter(Review.provider_id == provider_id).all()