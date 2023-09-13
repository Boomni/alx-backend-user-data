#!/usr/bin/env python3
"""
Module to create an SQLAlchemy model
named User for a database table named users
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """Class for users table"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250))
    session_id = Column(String(250))
    reset_token = Column(String(250))
