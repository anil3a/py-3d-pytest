# app/main.py

from fastapi import FastAPI
from .routers import router

app = FastAPI()

app.include_router(router)
