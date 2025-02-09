"""
This module contains the API routes for the files endpoints.
"""

import logging
from pathlib import Path

from fastapi import APIRouter, HTTPException

CURRENT_DIR = Path(__file__).parent

logger = logging.getLogger()
router = APIRouter()


@router.get("/filenames", response_model=list[str], tags=["files"])
async def get_data_filenames():
    logging.info("Getting data filenames")
    try:
        file_names = (CURRENT_DIR.parent / "data").rglob("*.json")
    except Exception as e:
        logging.error(f"Error getting data filenames: {e}")
        raise HTTPException(status_code=500, detail="Error getting data filenames")
    return [file_name.name for file_name in file_names]
