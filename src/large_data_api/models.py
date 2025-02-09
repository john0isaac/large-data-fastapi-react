"""
This module contains the Pydantic models for the API.
"""

from sqlmodel import Field, SQLModel


class DataBase(SQLModel):
    name: str
    description: str
    value: int


class Data(DataBase, table=True):
    id: int = Field(primary_key=True)


class CreateResponse(SQLModel):
    message: str
