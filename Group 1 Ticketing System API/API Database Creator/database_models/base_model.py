import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker

if sqlalchemy.__version__ < '2.0.0':
    raise ValueError('Please upgrade your version of SQLAlchemy to 2.0.0 or greater')

Base = declarative_base()

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go one level up
parent_dir = os.path.dirname(current_dir)
# Go another level up
parent_dir = os.path.dirname(parent_dir)
database_directory = parent_dir + "\API Project"
# Construct the full path for the database
Base.db_path = os.path.join(database_directory, 'it_ticketing_system.db')

Base.engine = create_engine(f'sqlite:///{Base.db_path}', echo=True)
