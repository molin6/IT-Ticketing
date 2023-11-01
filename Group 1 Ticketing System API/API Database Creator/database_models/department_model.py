from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from database_models.base_model import Base

class Department(Base):
    __tablename__ = 'dim_departments'
    
    department_id = Column(Integer, primary_key=True, autoincrement=True)
    organization_id = Column(Integer, ForeignKey('dim_organizations.organization_id'))
    name = Column(String, nullable=False)
    phone_number = Column(String)
    email_address = Column(String, nullable=False)
    
    # Relationships
    users = relationship('User', back_populates='department')
    organization = relationship('Organization', back_populates='departments')

    Session = sessionmaker(bind=Base.engine)

    def __repr__(self):
        return f'Department(id={self.department_id}, Name={self.name}, Organization={self.organization.name})'
