from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from models.base_model import Base

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
    technician = relationship('Technician', uselist=False, back_populates='user')
    organization = relationship('Organization', back_populates='users')
    department = relationship('Department', back_populates='users')

def read_user_ticket_counts(user_id=None):
    '''
    TODO: Insert tooltip documentation here
    '''
    db = Base.SessionLocal
    query = db.query(Base.user_model.User).join(Base.ticket_model.Ticket)
    user_data = []
    if not user_id:
        users = query.all()
    else:
        users = query.filter(Base.user_model.User.user_id == user_id).all()

    for row in users:
        ticket_count = len(row.tickets)
        user = row.first_name + ' ' + row.last_name + ' Ticket Count: ' + str(ticket_count)
        user_data.append(user)

    db.close()
    return user_data
