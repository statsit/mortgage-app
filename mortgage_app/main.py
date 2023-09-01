import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mortgage_app.api import mortgages
from mortgage_app.db import database, engine, metadata

metadata.create_all(engine)

app = FastAPI()

origins = ["http://localhost:3000", "http://10.0.0.103:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(mortgages.router, prefix="/mortgages", tags=["mortgages"])