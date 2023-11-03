from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from models.base_model import Base
from models.ticket_model import Ticket

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
    technician = relationship('Technician', uselist=False, back_populates='user', foreign_keys='Technician.technician_user_id')
    organization = relationship('Organization', back_populates='users')
    department = relationship('Department', back_populates='users')
    technician_manager = relationship('Technician', uselist=False, back_populates='manager', foreign_keys='Technician.manager_user_id')

    Session = sessionmaker(bind=Base.engine)

    @classmethod
    def read_user_ticket_counts(cls, user_id=None):
        '''
        Returns the first and last names of all the users along with their ticket counts
        
        param: user_id - optional parameter to filter by user_id
        '''

        with cls.Session() as session:
            query = session.query(cls).join(Ticket)
            user_data = []
            if not user_id:
                users = query.all()
            else:
                users = query.filter(User.user_id == user_id).all()

            for row in users:
                ticket_count = len(row.tickets)
                user = {
                    'First Name' : row.first_name,
                    'Last Name' : row.last_name,
                    'Ticket Count' : str(ticket_count)}
                user_data.append(user)

        return user_data
    
    #show (param) of records in the User tables
    @classmethod
    def read_users(cls):
        with cls.Session() as session:
            query = session.query(cls).all()
            users = []
            for row in query:
                user = {
                    
                    'Organization ID' : row.organization_id,
                    'Department ID' : row.department_id,
                    'Last Name' : row.last_name,
                    'First Name' : row.first_name,
                    'Phone Number' : row.phone_number,
                    'Email Address' : row.email_address,
                    'Title' : row.title}
                users.append(user)

        return users
    
    #delete a record in the User table
    @classmethod
    def delete_user(cls, user_id):
        with cls.Session() as session:
            user = session.query(cls).filter(User.user_id == user_id).first()
            if user is None:
                return {'Error': 'User not found', 'status': 404}
            session.delete(user)
            session.commit()
        return True
