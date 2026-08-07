from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Welcome to EconoCausal API"
    }