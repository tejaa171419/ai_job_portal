from sqlalchemy import text

from app.db.database import engine
from fastapi import FastAPI

app = FastAPI(
    title="AI Job Search Portal",
    description="AI-powered job discovery and matching platform",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "AI Job Search Portal API is running",
        "version": "1.0.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }



@app.get("/health/db")
def database_health():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {
            "database": result.scalar()
        }