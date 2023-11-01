from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from models.base_model import Base
from models.ticket_model import Ticket

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

    Session = sessionmaker(bind=Base.engine)


    def __repr__(self):
        return f'Department(id={self.department_id}, Name={self.name}, Organization={self.organization.name})'

    @classmethod
    def read_department_avg_resolution_time(cls):
        '''
        Retrieve the average resolution times for each department.
        '''
        with cls.Session() as session:
            query = session.query(Department.name, func.avg(Ticket.close_date_time - Ticket.open_date_time).label('avg_resolution_time_minutes'))\
                .join(Ticket, Department.department_id == Ticket.department_id)\
                .group_by(Department.name)
            
            results = query.all()

            departments = []
            for department_name, avg_resolution_time_minutes in results:
                departments.append(department_name + ' ' + str(avg_resolution_time_minutes))

        return departments
    
    #show (param) of records in the Department tables
    @classmethod
    def read_departments(cls):
        with cls.Session() as session:
            query = session.query(cls).all()
            departments = []
            for row in query:
                department = row.department_id, row.organization_id, row.name, row.phone_number, row.email_address
                departments.append(department)

        return departments