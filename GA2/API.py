from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, joinedload
import G1_common_tools as tools
import table_structures as tables

tools.install_required_packages()

# Database setup
DATABASE_URL = "sqlite:///it_ticketing_system.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI setup
app = FastAPI(
    title="IT Ticketing System API",
    description="API for Group 1's IT Ticketing System",
    version="0.1",
)


