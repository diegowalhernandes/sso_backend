from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    user_type: Optional[str] = "client"

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class ProviderProfileBase(BaseModel):
    category: str
    description: str
    hourly_rate: float

class ProviderProfileCreate(ProviderProfileBase):
    pass

class ProviderProfile(ProviderProfileBase):
    id: int
    user_id: int
    rating: float

    class Config:
        from_attributes = True

class ServiceRequestBase(BaseModel):
    provider_id: int
    description: str
    scheduled_date: str

class ServiceRequestCreate(ServiceRequestBase):
    pass

class ServiceRequest(ServiceRequestBase):
    id: int
    client_id: int
    status: str

    class Config:
        from_attributes = True

class ReviewBase(BaseModel):
    provider_id: int
    rating: int
    comment: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    client_id: int

    class Config:
        from_attributes = True