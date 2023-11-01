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

            organizationticket = []
            for row in results:
                organizationticket.append(row.organization.name + ' ' + str(len(row.tickets)))

        return organizationticket
    
    #show (param) of records in the Organization tables
    @classmethod
    def read_organizations(cls):
        with cls.Session() as session:
            query = session.query(cls).all()
            organizations = []
            for row in query:
                organization = row.organization_id, row.name, row.phone_number, row.email_address, row.state, row.city, row.zip_code, row.street_address
                organizations.append(organization)

        return organizations
