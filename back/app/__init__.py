from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import db
from app.api import router
from app.models import *

app = FastAPI()

app.include_router(router)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
