import asyncio
from fastapi import FastAPI

from mortgage_app.api import mortgages
from mortgage_app.db import database, engine, metadata

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(mortgages.router, prefix="/mortgages", tags=["mortgages"])