from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.core.security import get_current_user
from app.schemas import ServiceRequest, ServiceRequestCreate
from app.services.service_requests import create_service_request, get_service_requests, update_request_status

router = APIRouter(prefix="/service_requests", tags=["service_requests"])

@router.post("/", response_model=ServiceRequest)
async def create_request(
    request: ServiceRequestCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_service_request(db, request, current_user.id)

@router.get("/", response_model=List[ServiceRequest])
async def list_requests(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_service_requests(db, current_user.id, current_user.user_type)

@router.put("/{request_id}/status", response_model=ServiceRequest)
async def update_status(
    request_id: int,
    status: str,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return update_request_status(db, request_id, status, current_user.id)