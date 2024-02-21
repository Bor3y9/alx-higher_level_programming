#!/usr/bin/python3
"""The class definition of a City"""
from sqlalchemy import create_engine, Column, String, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class City(Base):
    """Defines the state class"""
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', VARCHAR(128), nullable=False)
    state_id = Column("state_id",Integer, ForeignKey('state.id'), nullable=False)
