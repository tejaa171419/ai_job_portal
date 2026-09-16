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