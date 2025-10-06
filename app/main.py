# app/main.py
from fastapi import FastAPI
from app.routes import users
from app.core.database import init_indexes
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI(title=os.getenv("APP_NAME", "FastAPI App"))

app.include_router(users.router)

@app.on_event("startup")
async def startup_event():
    await init_indexes()

@app.get("/")
def root():
    return {"message": "API funcionando correctamente 🚀"}
