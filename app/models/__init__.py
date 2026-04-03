from sqlalchemy import Column, Integer, String, Enum, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    user_type = Column(Enum("client", "provider", name="user_type_enum"))

    # Relationships
    provider_profile = relationship("ProviderProfile", back_populates="user", uselist=False)
    service_requests_as_client = relationship("ServiceRequest", back_populates="client", foreign_keys="ServiceRequest.client_id")
    service_requests_as_provider = relationship("ServiceRequest", back_populates="provider", foreign_keys="ServiceRequest.provider_id")
    reviews_given = relationship("Review", back_populates="client", foreign_keys="Review.client_id")
    reviews_received = relationship("Review", back_populates="provider", foreign_keys="Review.provider_id")

class ProviderProfile(Base):
    __tablename__ = "provider_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    category = Column(String)
    description = Column(Text)
    hourly_rate = Column(Float)
    rating = Column(Float, default=0.0)

    # Relationships
    user = relationship("User", back_populates="provider_profile")

class ServiceRequest(Base):
    __tablename__ = "service_requests"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("users.id"))
    provider_id = Column(Integer, ForeignKey("users.id"))
    status = Column(Enum("pending", "accepted", "completed", "canceled", name="status_enum"))
    description = Column(Text)
    scheduled_date = Column(DateTime)

    # Relationships
    client = relationship("User", back_populates="service_requests_as_client", foreign_keys=[client_id])
    provider = relationship("User", back_populates="service_requests_as_provider", foreign_keys=[provider_id])

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("users.id"))
    provider_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Integer)
    comment = Column(Text)

    # Relationships
    client = relationship("User", back_populates="reviews_given", foreign_keys=[client_id])
    provider = relationship("User", back_populates="reviews_received", foreign_keys=[provider_id])