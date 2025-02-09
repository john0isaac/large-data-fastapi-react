"""
FastAPI for large data API
"""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import TypedDict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.engine import Engine
from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./test_db.sqlite"


class State(TypedDict):
    engine: Engine


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[State]:
    engine = create_engine(DATABASE_URL, echo=False)
    SQLModel.metadata.create_all(engine)
    try:
        yield {"engine": engine}
    finally:
        engine.dispose()


def create_app():
    logging.basicConfig(
        handlers=[logging.StreamHandler(), logging.FileHandler("large_data.log")],
        format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    app = FastAPI(title="Large Data API", lifespan=lifespan)

    from large_data_api.routers import data

    app.include_router(data.router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
