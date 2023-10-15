from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from models.base_model import Base

class Ticket(Base):
    __tablename__ = 'fact_tickets'
    
    ticket_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('dim_users.user_id'))
    department_id = Column(Integer, ForeignKey('dim_departments.department_id'))
    prior_ticket_id = Column(Integer)
    ticket_category = Column(String, nullable=False)
    open_date_time = Column(DateTime, nullable=False)
    close_date_time = Column(DateTime)
    status = Column(String)
    description = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    
    # Relationships
    user = relationship('User', back_populates='tickets')
    ticket_lines = relationship('TicketLine', back_populates='ticket')

    Session = sessionmaker(bind=Base.engine)