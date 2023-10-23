from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from datetime import timedelta
from models.base_model import Base
from models.user_model import User
from models.ticket_line_model import TicketLine
from models.ticket_model import Ticket

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

    @classmethod
    def read_technician_names(cls):
        with cls.Session() as session:
            query = session.query(User).join(cls).all()
            technicians = []
            for row in query:
                technician = row.first_name + ' ' + row.last_name
                technicians.append(technician)

        return technicians

    @classmethod
    def read_technician_avg_ticket_times(cls):
        with cls.Session() as session:
            query = session.query(cls).join(TicketLine).join(User)
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
        return technicians

    @classmethod
    def read_technician_ticketinfo(cls):
        '''
        Retrieve and print ticket information for each technician based on technician ID.
        '''
        desired_technician_id = 1

        with cls.Session() as session:
            query = session.query(Ticket.ticket_id, Ticket.subject, Ticket.open_date_time, Ticket.close_date_time)\
                .join(TicketLine, Ticket.ticket_id == TicketLine.ticket_id)\
                .filter(TicketLine.technician_id == desired_technician_id)
        
            results = query.all()

            technicianticket = []
            for ticket_id, subject, open_date_time, close_date_time in results:
                technicianticket.append(' Ticket ID: ' + str(ticket_id) + ' Subject: ' + subject + ' Open Date: ' + str(open_date_time) + ' Closed Date ' + str(close_date_time))

        return technicianticket
    
    @classmethod
    def select_technicians(cls, limit):
        with cls.Session() as session:
            query = session.query(cls).limit(limit).all()
            technicians = []
            for row in query:
                technician = {
                    'technician_id': row.technician_id,
                    'user_id': row.user_id,
                    'manager_id': row.manager_id
                }
                technicians.append(technician)
        return technicians
    
    @classmethod
    def update_technician_manager(cls, technician_id, manager_id):
        with cls.Session() as session:
            technician = session.query(cls).filter(cls.technician_id == technician_id).first()
            technician.manager_id = manager_id
            session.commit()

            for row in session.query(cls).filter(cls.technician_id == technician_id).all():
                technician = {
                    'technician_id': row.technician_id,
                    'user_id': row.user_id,
                    'manager_id': row.manager_id
                }

            return technician

    @classmethod
    def get_technicians_manager(cls, technician_id):
        '''
        Retrieve the manager of a technician

        params: technician_id - the id of the technician whose manager is getting retrieved
        '''
        with cls.Session() as session:
            manager = session.query(cls).filter(cls.technician_id == technician_id).first().manager
            manager_name = manager.first_name + ' ' + manager.last_name

        return manager_name
