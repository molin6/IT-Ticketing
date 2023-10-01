from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class Organization(Base):
    __tablename__ = 'dim_organizations'
    
    organization_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone_number = Column(String)
    email_address = Column(String, nullable=False)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    zip_code = Column(Integer, nullable=False)
    street_address = Column(String, nullable=False)
    
    # Relationships
    users = relationship('User', back_populates='organization')
    departments = relationship('Department', back_populates='organization')

    def __repr__(self):
        return f'Organization(id={self.organization_id}, Name={self.name}, city={self.city}, state={self.state})'


class Department(Base):
    __tablename__ = 'dim_departments'
    
    department_id = Column(Integer, primary_key=True, autoincrement=True)
    organization_id = Column(Integer, ForeignKey('dim_organizations.organization_id'))
    name = Column(String, nullable=False)
    phone_number = Column(String)
    email_address = Column(String, nullable=False)
    
    # Relationships
    users = relationship('User', back_populates='department')
    organization = relationship('Organization', back_populates='departments')

    def __repr__(self):
        return f'Department(id={self.department_id}, Name={self.name}, Organization={self.organization.name})'


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
    ticket_lines = relationship('TicketLine', back_populates='technician')
    technician_details = relationship('Technician', uselist=False, back_populates='user')
    organization = relationship('Organization', back_populates='users')
    department = relationship('Department', back_populates='users')


class Technician(Base):
    __tablename__ = 'dim_technicians'
    
    technician_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('dim_users.user_id'))
    manager_id = Column(Integer)
    
    # Relationships
    user = relationship('User', back_populates='technician_details')


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


class TicketLine(Base):
    __tablename__ = 'fact_ticket_lines'
    
    ticket_line_id = Column(Integer, primary_key=True, autoincrement=True)
    ticket_id = Column(Integer, ForeignKey('fact_tickets.ticket_id'))
    technician_id = Column(Integer, ForeignKey('dim_users.user_id'))
    assignment_date_time = Column(DateTime, nullable=False)
    completion_date_time = Column(DateTime)
    notes = Column(String)
    
    # Relationships
    technician = relationship('User', back_populates='ticket_lines')
    ticket = relationship('Ticket', back_populates='ticket_lines')