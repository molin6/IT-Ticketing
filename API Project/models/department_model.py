from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, relationship
from models.base_model import Base

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

def read_department_avg_resolution_time():
    '''
    Retrieve the average resolution times for each department.
    '''
    db = Base.SessionLocal
    query = db.query(Base.department_model.Department.name, func.avg(Base.ticket_model.Ticket.close_date_time - Base.ticket_model.Ticket.open_date_time).label('avg_resolution_time_minutes'))\
    .join(Base.ticket_model.Ticket, Base.department_model.Department.department_id == Base.ticket_model.Ticket.department_id)\
    .group_by(Base.department_model.Department.name)
    
    results = query.all()

    departments = []
    for department_name, avg_resolution_time_minutes in results:
        departments.append(department_name + ' ' + str(avg_resolution_time_minutes))

    db.close()
    return departments