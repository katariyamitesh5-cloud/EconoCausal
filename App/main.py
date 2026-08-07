from fastapi import FastAPI

app = FastAPI(
    title="EconoCausal API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to EconoCausal API"
    }