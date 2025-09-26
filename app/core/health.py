from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["welcome"])
def welcome():
    return {"message": "Welcome to the FastAPI UV Backend"}

@router.get("/health", tags=["health"])
def health():
    return {"status": "ok"}
