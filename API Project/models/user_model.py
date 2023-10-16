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
    technician = relationship('Technician', uselist=False, back_populates='user', foreign_keys='Technician.user_id')
    organization = relationship('Organization', back_populates='users')
    department = relationship('Department', back_populates='users')
    technician_manager = relationship('Technician', uselist=False, back_populates='manager', foreign_keys='Technician.manager_id')

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
                user = row.first_name + ' ' + row.last_name + ' Ticket Count: ' + str(ticket_count)
                user_data.append(user)

        return user_data
