from fastapi import FastAPI
from app.db import db
from app.api import router
from app.models import *

app = FastAPI()

app.include_router(router)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
