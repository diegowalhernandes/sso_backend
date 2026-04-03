from sqlalchemy.orm import Session
from datetime import datetime
from app.models import ServiceRequest
from app.schemas import ServiceRequestCreate

def create_service_request(db: Session, request: ServiceRequestCreate, client_id: int):
    db_request = ServiceRequest(
        client_id=client_id,
        provider_id=request.provider_id,
        status="pending",
        description=request.description,
        scheduled_date=datetime.fromisoformat(request.scheduled_date)
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

def get_service_requests(db: Session, user_id: int, user_type: str):
    if user_type == "client":
        return db.query(ServiceRequest).filter(ServiceRequest.client_id == user_id).all()
    else:
        return db.query(ServiceRequest).filter(ServiceRequest.provider_id == user_id).all()

def update_request_status(db: Session, request_id: int, status: str, user_id: int):
    request = db.query(ServiceRequest).filter(ServiceRequest.id == request_id).first()
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    # Check permissions
    if request.client_id != user_id and request.provider_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized")
    request.status = status
    db.commit()
    db.refresh(request)
    return request