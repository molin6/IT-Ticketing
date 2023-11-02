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
    
    #show (param) of records in the Ticket Line tables
    @classmethod
    def read_ticket_lines(cls):
        
        with cls.Session() as session:
            query = session.query(cls).all()
            ticket_lines = []
            for row in query:
                ticket_line = {
                'Ticket ID' : row.ticket_id,
                'Technician ID' : row.technician_id,
                'Assignment Date Time' : row.assignment_date_time,
                'Completion Date Time' : row.completion_date_time,
                'Notes' : row.notes
                }
                
                ticket_lines.append(ticket_line)

        return ticket_lines