from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import timedelta
from models.base_model import Base

class Technician(Base):
    __tablename__ = 'dim_technicians'
    
    technician_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('dim_users.user_id'))
    manager_id = Column(Integer)
    
    # Relationships
    user = relationship('User', back_populates='technician')
    ticket_lines = relationship('TicketLine', back_populates='technician')

def read_technician_names():
    db = Base.SessionLocal
    query = db.query(Base.user_model.User).join(Base.technician_model.Technician).all()

    technicians = []
    for row in query:
        technician = row.first_name + ' ' + row.last_name
        technicians.append(technician)
    db.close()
    return technicians

def read_technician_avg_ticket_times():
    db = Base.SessionLocal
    query = db.query(Base.technician_model.Technician).join(Base.ticket_line_model.TicketLine).join(Base.user_model.User)
    query.all()
    technicians = []
    for row in query:
        ticket_durations = []
        for x in row.ticket_lines:
            interval = x.completion_date_time - x.assignment_date_time
            ticket_durations.append(interval)
        total_seconds = sum(interval.total_seconds() for interval in ticket_durations)
        average_seconds = total_seconds / len(ticket_durations) if ticket_durations else 0
        average_interval = timedelta(seconds=average_seconds)
        technician = row.user.first_name + ' ' + row.user.last_name + ' - Average Ticket Time: ' + str(average_interval)
        technicians.append(technician)
    db.close()
    return technicians

def read_technician_ticketinfo():
    '''
    Retrieve and print ticket information for each technician based on technician ID.
    '''
    db = Base.SessionLocal

    desired_technician_id = 1

    query = db.query(Base.ticket_model.Ticket.ticket_id, Base.ticket_model.Ticket.subject, Base.ticket_model.Ticket.open_date_time, Base.ticket_model.Ticket.close_date_time)\
    .join(Base.ticket_line_model.TicketLine, Base.ticket_model.Ticket.ticket_id == Base.ticket_line_model.TicketLine.ticket_id)\
    .filter(Base.ticket_line_model.TicketLine.technician_id == desired_technician_id)
    
    results = query.all()

    technicianticket = []
    for ticket_id, subject, open_date_time, close_date_time in results:
        technicianticket.append(' Ticket ID: ' + str(ticket_id) + ' Subject: ' + subject + ' Open Date: ' + str(open_date_time) + ' Closed Date ' + str(close_date_time))

    db.close()
    return technicianticket