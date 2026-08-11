import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import text
from app.core.db import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))
        print('Database connected')

        yield

        await engine.dispose()
        print('Database disconnected')

restaurant_app = FastAPI(title="Restaurant AI Copilot", version="1.0.0")


@restaurant_app.get("/")
async def root():
    return {"message": "Restaurant AI Copilot API"}


@restaurant_app.get("/healthz")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(restaurant_app, host='127.0.0.1', port=8000)
