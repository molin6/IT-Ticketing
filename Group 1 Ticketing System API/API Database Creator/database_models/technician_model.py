from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from database_models.base_model import Base

class Technician(Base):
    __tablename__ = 'dim_technicians'
    
    technician_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('dim_users.user_id'))
    manager_id = Column(Integer, ForeignKey('dim_users.user_id'))
    
    # Relationships
    user = relationship('User', back_populates='technician', foreign_keys='Technician.user_id')
    ticket_lines = relationship('TicketLine', back_populates='technician')
    manager = relationship('User', back_populates='technician_manager', foreign_keys='Technician.manager_id')

    Session = sessionmaker(bind=Base.engine)
