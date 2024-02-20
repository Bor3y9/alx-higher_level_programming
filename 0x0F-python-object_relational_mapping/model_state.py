#!/usr/bin/python3
"""The class definition of a State"""
from sqlalchemy import create_engine, Column, String, Integer, VARCHAR
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class State(Base):
    """Defines the state class"""
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', VARCHAR(128), nullable=False)
