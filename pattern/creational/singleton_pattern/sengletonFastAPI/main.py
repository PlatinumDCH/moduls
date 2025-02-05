from fastapi import FastAPI
from contextlib import asynccontextmanager
from pattern.creational.singleton_pattern.sengletonFastAPI.database import db
from pattern.creational.singleton_pattern.sengletonFastAPI.register import APIRouterManager



@asynccontextmanager
async def lifespan(app:FastAPI):
    await db.crate_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/root")
async def predict():
    return {"message": "home page"}

APIRouterManager.attach(app)