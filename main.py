# app/main.py
from fastapi import FastAPI
from app.routes.livestream import router as livestream_router

app = FastAPI(
    title="Livestream Service",
    version="1.0.0",
)

app.include_router(livestream_router, prefix="/livestreams", tags=["Livestreams"])

@app.get("/")
async def root():
    return {"message": "Livestream service is up and running!"}
