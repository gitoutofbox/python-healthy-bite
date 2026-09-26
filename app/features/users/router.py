from fastapi import APIRouter
from app.core.auth import createToken, verifyToken

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/login")
def login():
    return {
        "access_token": createToken({"user": "admin"}),
        "token_type": "Bearer"
    }