import sqlalchemy
from sqlalchemy.orm import DeclarativeBase

if sqlalchemy.__version__ < '2.0.0':
    raise ValueError('Please upgrade your version of SQLAlchemy to 2.0.0 or greater')

class Base(DeclarativeBase):
    pass