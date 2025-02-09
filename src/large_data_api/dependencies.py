from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends, Request
from sqlalchemy.engine import Engine
from sqlmodel import Session


async def get_engine(
    request: Request,
) -> AsyncGenerator[Engine, None]:
    yield request.state.engine


async def get_session(engine: Annotated[Engine, Depends(get_engine)]) -> AsyncGenerator[Session, None]:
    with Session(engine) as session:
        yield session


DBSession = Annotated[Session, Depends(get_session)]
