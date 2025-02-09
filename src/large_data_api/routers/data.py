"""
This module contains the API routes for the data endpoints.
"""

import logging
from pathlib import Path

from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select

from large_data_api.dependencies import DBSession
from large_data_api.models import CreateResponse, Data
from large_data_api.utils.generate_data import load_data_from_file

CURRENT_DIR = Path(__file__).parent

logger = logging.getLogger()
router = APIRouter()


@router.get("/data", response_model=list[Data])
async def get_data(session: DBSession):
    logging.info("Getting data")
    try:
        data = session.exec(select(Data)).all()
    except (Exception, SQLAlchemyError) as e:
        logging.error(f"Error getting data: {e}")
        raise HTTPException(status_code=500, detail="Error getting data")
    return data


@router.get("/data/populate/{file_name}", response_model=CreateResponse)
async def populate_data(session: DBSession, file_name: str = "10k_random_data.json"):
    logging.info("Populating data")
    raw_data = load_data_from_file(CURRENT_DIR.parent / "data" / file_name)
    try:
        # Cleanup existing data
        for data in raw_data:
            session.add(Data(**data))
        session.commit()
    except (Exception, SQLAlchemyError) as e:
        logging.error(f"Error populating data: {e}")
        raise HTTPException(status_code=500, detail="Error populating data")
    return CreateResponse(message="Data populated successfully")
