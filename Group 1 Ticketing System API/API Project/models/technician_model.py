from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, aliased
from sqlalchemy.orm.exc import NoResultFound
from datetime import timedelta
from models.base_model import Base
from models.user_model import User
from models.ticket_line_model import TicketLine
from models.ticket_model import Ticket

class Technician(Base):
    __tablename__ = 'dim_technicians'
    
    technician_id = Column(Integer, primary_key=True, autoincrement=True)
    technician_user_id = Column(Integer, ForeignKey('dim_users.user_id'))
    manager_user_id = Column(Integer, ForeignKey('dim_users.user_id'))
    
    # Relationships
    user = relationship('User', back_populates='technician', foreign_keys='Technician.technician_user_id')
    ticket_lines = relationship('TicketLine', back_populates='technician')
    manager = relationship('User', back_populates='technician_manager', foreign_keys='Technician.manager_user_id')

    Session = sessionmaker(bind=Base.engine)

    @classmethod
    def read_technician_names(cls):
        with cls.Session() as session:
            query = session.query(User).join(cls, User.user_id == cls.technician_user_id).all()
            technicians = []
            for row in query:
                technician = {
                    'first_name': row.first_name,
                    'last_name': row.last_name
                }
                technicians.append(technician)

        return technicians

    @classmethod
    def read_technician_avg_ticket_times(cls):
        with cls.Session() as session:
            query = session.query(cls).join(TicketLine).join(User, User.user_id == cls.technician_user_id)
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
                technician = {
                    'technician_id': row.technician_id,
                    'first_name': row.user.first_name,
                    'last_name': row.user.last_name,
                    'average_ticket_time': str(average_interval)
                }
                technicians.append(technician)
        return technicians

    @classmethod
    def read_technician_ticketinfo(cls, technician_id):
        '''
        Retrieve and print ticket information for each technician based on technician ID.
        '''
        with cls.Session() as session:
            try:
                # Check if the technician exists
                session.query(Technician).filter(Technician.technician_id == technician_id).one()
            except NoResultFound:
                # If the technician doesn't exist, return None
                return None
            
            query = session.query(Ticket.ticket_id, Ticket.prior_ticket_id, Ticket.subject, Ticket.status,\
                                   Ticket.open_date_time, Ticket.close_date_time, Ticket.ticket_category, TicketLine.notes)\
                .join(TicketLine, Ticket.ticket_id == TicketLine.ticket_id)\
                .filter(TicketLine.technician_id == technician_id)

            results = query.all()

            techniciantickets = []
            for row in results:
                technicianticket = {
                    'ticket_id': row.ticket_id,
                    'prior_ticket_id': row.prior_ticket_id,
                    'subject': row.subject,
                    'status': row.status,
                    'open_date_time': row.open_date_time,
                    'close_date_time': row.close_date_time,
                    'ticket_category': row.ticket_category,
                    'notes': row.notes
                }
                techniciantickets.append(technicianticket)
        return techniciantickets
    
    @classmethod
    def select_technicians(cls, limit):
        with cls.Session() as session:
            query = session.query(cls).limit(limit).all()
            technicians = []
            for row in query:
                technician = {
                    'technician_id': row.technician_id,
                    'technician_user_id': row.technician_user_id,
                    'manager_user_id': row.manager_user_id
                }
                technicians.append(technician)
        return technicians
    
    @classmethod
    def update_technician_manager(cls, technician_id, manager_user_id):
        with cls.Session() as session:
            try:
                # Check if the technician exists
                session.query(Technician).filter(Technician.technician_id == technician_id).one()
            except NoResultFound:
                # If the technician doesn't exist, return None
                return None

            try:
                # Check if the manager exists
                # session.query(User).filter(User.user_id == manager_user_id).one()
                result = session.query(User).filter(User.user_id == manager_user_id).one_or_none()
            except NoResultFound:
                # If the manager doesn't exist, return None
                return None
            if result is None:
                return None

            technician = session.query(cls).filter(cls.technician_id == technician_id).first()
            technician.manager_user_id = manager_user_id
            session.commit()

            for row in session.query(cls).filter(cls.technician_id == technician_id).all():
                technician = {
                    'technician_id': row.technician_id,
                    'technician_user_id': row.technician_user_id,
                    'manager_user_id': row.manager_user_id
                }

            return technician

    @classmethod
    def get_technicians_manager(cls, technician_id):
        '''
        Retrieve the manager of a technician

        params: technician_id - the id of the technician whose manager is getting retrieved
        '''

        UserTechnician = aliased(User, name='UserTechnician')

        with cls.Session() as session:
            try:
                # Check if the technician exists
                session.query(Technician).filter(Technician.technician_id == technician_id).one()
            except NoResultFound:
                # If the technician doesn't exist, return None
                return None

            # Get the manager of the technician
            query = session.query(
                Technician.technician_id,
                UserTechnician.first_name.label('technician_first_name'),
                UserTechnician.last_name.label('technician_last_name'),
                Technician.manager_user_id,
                User
            )\
                .join(User, User.user_id == Technician.manager_user_id)\
                .join(UserTechnician, UserTechnician.user_id == Technician.technician_user_id)\
                .filter(cls.technician_id == technician_id)
            result = query.first()

            if result is None or result.manager_user_id is None:
                return None

            manager = {
                'technician_id': result.technician_id,
                'technician_first_name': result.technician_first_name,
                'technician_last_name': result.technician_last_name,
                'manager': {column.name: getattr(result.User, column.name) for column in User.__table__.columns}
            }
        return manager

