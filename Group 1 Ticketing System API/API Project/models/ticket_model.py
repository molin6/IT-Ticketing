from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from models.base_model import Base
from datetime import datetime

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

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    #show (param) of records in the Ticket tables
    @classmethod
    def read_tickets_10(cls):
        with cls.Session() as session:
            query = session.query(cls).all()
            tickets = []
            for row in query:
                ticket = row.ticket_id, row.user_id, row.department_id, row.prior_ticket_id, row.ticket_category\
                , row.open_date_time, row.close_date_time, row.status, row.description, row.subject
                tickets.append(ticket)

        return tickets
    
    #Adds a new ticket
    @classmethod
    def create_ticket(cls, ticket_data):
        with cls.Session() as session:
            open_date_time1 = datetime.strptime(ticket_data['open_date_time'], '%a, %d %b %Y %H:%M:%S %Z')
            close_date_time1 = datetime.strptime(ticket_data['close_date_time'], '%a, %d %b %Y %H:%M:%S %Z')
            new_ticket = cls(user_id=ticket_data['user_id']
                             , department_id=ticket_data['department_id']
                             , prior_ticket_id=ticket_data['prior_ticket_id']
                             , ticket_category=ticket_data['ticket_category']
                             , open_date_time=open_date_time1
                             , close_date_time=close_date_time1
                             , status=ticket_data['status']
                             , description=ticket_data['description']
                             , subject=ticket_data['subject'])
            session.add(new_ticket)
            session.commit()
            session.refresh(new_ticket)
            return new_ticket
        

    #Updates a ticket
    @classmethod
    def update_ticket(cls, ticket_id, ticket_data):
        with cls.Session() as session:
            ticket = session.query(cls).filter(cls.ticket_id == ticket_id).first()
            open_date_time1 = datetime.strptime(ticket_data['open_date_time'], '%a, %d %b %Y %H:%M:%S %Z')
            close_date_time1 = datetime.strptime(ticket_data['close_date_time'], '%a, %d %b %Y %H:%M:%S %Z')
            ticket.user_id = ticket_data['user_id']
            ticket.department_id = ticket_data['department_id']
            ticket.prior_ticket_id = ticket_data['prior_ticket_id']
            ticket.ticket_category = ticket_data['ticket_category']
            ticket.open_date_time = open_date_time1
            ticket.close_date_time = close_date_time1
            ticket.status = ticket_data['status']
            ticket.description = ticket_data['description']
            ticket.subject = ticket_data['subject']
            session.commit()
            session.refresh(ticket)
            return ticket

        