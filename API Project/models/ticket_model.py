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

    #show (param) of records in the Ticket tables
    @classmethod
    def read_tickets_10(cls):
        with cls.Session() as session:
            query = session.query(cls).all()
            tickets = []
            for row in query:
                ticket = row.ticket_id, row.user_id, row.department_id, row.prior_ticket_id, row.ticket_category, row.open_date_time, row.close_date_time, row.status, row.description, row.subject
                tickets.append(ticket)

        return tickets