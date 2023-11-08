from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from models.base_model import Base
from models.user_model import User

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

    Session = sessionmaker(bind=Base.engine)

    def __repr__(self):
        return f'Organization(id={self.organization_id}, Name={self.name}, city={self.city}, state={self.state})'
    
    @classmethod
    def read_organizations_tickets_count(cls):
        '''
        Retrieve ticket counts for each organization.
        '''
        with cls.Session() as session:
            query = session.query(User).join(cls).group_by(cls.name)

            results = query.all()

            organizationtickets = []
            for row in results:
                organizationticket = {
                    'Organization Name': row.organization.name,
                    'Ticket Count': str(len(row.tickets))}
                organizationtickets.append(organizationticket)

        return organizationtickets
    
    #show (param) of records in the Organization tables
    @classmethod
    def read_organizations(cls, start, limit):
        with cls.Session() as session:
            query = session.query(cls)
            if start is not None:
                query = query.offset(start)
            if limit is not None:
                query = query.limit(limit)
            organizations = []
            for row in query.all():
                organization = {
                    'Organization ID' : row.organization_id, 
                    'Name' : row.name, 
                    'Phone Number' : row.phone_number, 
                    'Email Address' : row.email_address, 
                    'State' : row.state, 
                    'City' : row.city, 
                    'ZipCode' : row.zip_code, 
                    'Street Adress' : row.street_address}
                organizations.append(organization)
        return organizations
