from fastapi import FastAPI
from app.features.users.router import router as users_router
from app.features.dishes.router import router as dishes_router

app = FastAPI(title="Enterprise E-Commerce API")

@app.get("/")
def home():
    return {"status": "ok"}

# Connect feature routers
app.include_router(users_router)
app.include_router(dishes_router)