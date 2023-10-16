from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from models.base_model import Base

class TicketLine(Base):
    __tablename__ = 'fact_ticket_lines'
    
    ticket_line_id = Column(Integer, primary_key=True, autoincrement=True)
    ticket_id = Column(Integer, ForeignKey('fact_tickets.ticket_id'))
    technician_id = Column(Integer, ForeignKey('dim_technicians.technician_id'))
    assignment_date_time = Column(DateTime, nullable=False)
    completion_date_time = Column(DateTime)
    notes = Column(String)
    
    # Relationships
    technician = relationship('Technician', back_populates='ticket_lines')
    ticket = relationship('Ticket', back_populates='ticket_lines')

    Session = sessionmaker(bind=Base.engine)
    
    #show first 10 records in the Ticket Line tables
    @classmethod
    def read_ticket_lines_10(cls):
        with cls.Session() as session:
            query = session.query(cls).limit(10)
            ticket_lines = []
            for row in query:
                ticket_line = row.ticket_id, row.technician_id, row.assignment_date_time, row.completion_date_time, row.notes
                ticket_lines.append(ticket_line)

        return ticket_lines