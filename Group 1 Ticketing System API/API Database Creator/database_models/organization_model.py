from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, sessionmaker
from database_models.base_model import Base

class Organization(Base):
    __tablename__ = 'dim_organizations'
    
    organization_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone_number = Column(String)
    email_address = Column(String, nullable=False)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    zip_code = Column(Integer, nullable=False)
    street_address = Column(String, nullable=False)
    
    # Relationships
    users = relationship('User', back_populates='organization')
    departments = relationship('Department', back_populates='organization')

    Session = sessionmaker(bind=Base.engine)

    def __repr__(self):
        return f'Organization(id={self.organization_id}, Name={self.name}, city={self.city}, state={self.state})'
