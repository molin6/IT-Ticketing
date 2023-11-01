from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from database_models.base_model import Base

class User(Base):
    __tablename__ = 'dim_users'
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    organization_id = Column(Integer, ForeignKey('dim_organizations.organization_id'))
    department_id = Column(Integer, ForeignKey('dim_departments.department_id'))
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    phone_number = Column(String)
    email_address = Column(String, nullable=False)
    title = Column(String)
    
    # Relationships
    tickets = relationship('Ticket', back_populates='user')
    technician = relationship('Technician', uselist=False, back_populates='user', foreign_keys='Technician.user_id')
    organization = relationship('Organization', back_populates='users')
    department = relationship('Department', back_populates='users')
    technician_manager = relationship('Technician', uselist=False, back_populates='manager', foreign_keys='Technician.manager_id')

    Session = sessionmaker(bind=Base.engine)
