from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.core.config import settings
from app.database import engine, create_tables
from app.routes import auth, users, providers, service_requests, reviews

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Service Marketplace API", version="1.0.0")

# CORS middleware - DEVE estar ANTES das rotas
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
    expose_headers=["Content-Type"],
    max_age=600,
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(providers.router)
app.include_router(service_requests.router)
app.include_router(reviews.router)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the application...")
    create_tables()

@app.get("/")
async def root():
    return {"message": "Service Marketplace API"}