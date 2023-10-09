from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from models.base_model import Base

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
    
def read_organizations_tickets_count():
    '''
    Retrieve ticket counts for each organization.
    '''
    db = Base.SessionLocal

    query = db.query(Base.user_model.User).join(Base.organization_model.Organization).group_by(Base.organization_model.Organization.name)

    results = query.all()

    organizationticket = []
    for row in results:
        organizationticket.append(row.organization.name + ' ' + str(len(row.tickets)))

    db.close()
    return organizationticket
