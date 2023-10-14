from models.base_model import Base
from models.department_model import Department
from models.organization_model import Organization
from models.technician_model import Technician
from models.ticket_line_model import TicketLine
from models.ticket_model import Ticket
from models.user_model import User
from models.department_model import Department
from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy.exc import SQLAlchemyError
from faker import Faker
import random
from utils import G1_common_tools as tools
import sqlite3
import os

engine = None
session = None
fake = Faker()
SessionLocal = None

def create_engine_and_database(reset_database: bool = False):

    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Go one level up
    parent_dir = os.path.dirname(current_dir)

    # Construct the full path for the database
    db_path = os.path.join(parent_dir, 'it_ticketing_system.db')

    if reset_database:
        drop_all_tables(db_path)

    global engine

    engine = create_engine(f'sqlite:///{db_path}', echo=True)
    if not database_exists(engine.url):
        create_database(engine.url)

    global session
    session = Session(engine)
    global SessionLocal
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(engine)

def drop_all_tables(db_path):
    cnn = sqlite3.connect(db_path)
    cur = cnn.cursor()
    table_names = []
    results = cur.execute("SELECT tbl_name FROM sqlite_master")
    for table_name in results:
        table_names.append(table_name[0])

    for table_name in table_names:
        cur.execute(f'DROP TABLE IF EXISTS {table_name}')
        print(f'Dropped table \'{table_name}\'')

    cnn.close()

def add_objects_to_db(objects: list):
    try:
        session.add_all(objects)
        session.commit()
        return True
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        session.rollback()
        return False
    
def seed_organizations(session: Session, num_organizations: int):
    organizations = []
    for _ in range(num_organizations):
        organization = Organization(
            name=fake.company(),
            phone_number=fake.phone_number(),
            email_address=fake.company_email(),
            state=fake.state_abbr(),
            city=fake.city(),
            zip_code=fake.zipcode(),
            street_address=fake.street_address(),
        )
        organizations.append(organization)
    return add_objects_to_db(organizations)

def seed_departments(session: Session, num_departments_per_organization: int, organizations: list):
    departments = []
    for organization in organizations:
        for _ in range(num_departments_per_organization):
            department = Department(
                organization_id=organization.organization_id,
                name=fake.bs(),
                phone_number=fake.phone_number(),
                email_address=fake.company_email(),
            )
            departments.append(department)
    return add_objects_to_db(departments)

def seed_users(session: Session, num_users_per_department: int, departments: list):
    users = []
    for department in departments:
        for _ in range(num_users_per_department):
            user = User(
                organization_id=department.organization_id,
                department_id=department.department_id,
                last_name=fake.last_name(),
                first_name=fake.first_name(),
                phone_number=fake.phone_number(),
                email_address=fake.email(),
                title=fake.job(),
            )
            users.append(user)
    return add_objects_to_db(users)

def seed_tickets(session: Session, users: list, num_tickets_per_user: int=None):
    tickets = []
    for user in users:
        user_ticket_count = 0
        if not num_tickets_per_user:
            user_ticket_count = random.randint(0, 5)
        else:
            user_ticket_count = num_tickets_per_user

        for _ in range(user_ticket_count):
            ticket = Ticket(
                user_id=user.user_id,
                department_id=user.department_id,
                ticket_category=fake.word(),
                open_date_time=fake.date_time_this_decade(),
                close_date_time=fake.date_time_this_decade(),
                status=fake.word(),
                description=fake.text(),
                subject=fake.sentence(),
            )
            tickets.append(ticket)
    return add_objects_to_db(tickets)

def seed_technicians(session: Session, users: list, num_technicians: int):
    technicians = []
    selected_users = random.sample(users, k=min(num_technicians, len(users)))

    for user in selected_users:
        technician = Technician(user_id=user.user_id)
        technicians.append(technician)

    return add_objects_to_db(technicians)

def seed_ticket_lines(session: Session, num_ticket_lines_per_ticket: int, tickets: list, technicians: list):
    ticket_lines = []
    for ticket in tickets:
        for _ in range(num_ticket_lines_per_ticket):
            technician = random.choice(technicians)

            ticket_line = TicketLine(
                ticket_id=ticket.ticket_id,
                technician_id=technician.technician_id,
                assignment_date_time=fake.date_time_this_decade(),
                completion_date_time=fake.date_time_this_decade(),
                notes=fake.text(),
            )
            ticket_lines.append(ticket_line)
    return add_objects_to_db(ticket_lines)

def print_database_definitions(db_file_name : str = 'it_ticketing_system.db'):
    cnn = sqlite3.connect(db_file_name)
    cur = cnn.cursor()
    tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

    for table in tables:
        print('------------------')
        print('Table Name: ' + table[0])
        print('------------------')
        columns = cur.execute(f'PRAGMA table_info(\'%s\');' % table[0]).fetchall()
        for column in columns:
            col_id, col_name, col_type, col_notnull, col_default, col_pk = column
            print(f"  Column: {col_name}")
            print(f"    Type: {col_type}")
            print(f"    Not Null: {tools.bool_to_yes_no(col_notnull)}")
            print(f"    Default Value: {col_default}")
            print(f"    Primary Key: {tools.bool_to_yes_no(col_pk)}")

    cnn.close()

def populate_database_tables():
    #Create the organizations:
    num_organizations = 5
    seed_organizations(session, num_organizations)
    organizations = session.query(Organization).all()

    #Create the departments:
    num_departments_per_organization = 3
    seed_departments(session, num_departments_per_organization, organizations)
    departments = session.query(Department).all()

    #Create the users:
    num_users_per_department = 10
    seed_users(session, 10, departments)
    users = session.query(User).all()

    #Create the tickets:
    # num_tickets_per_user = 5
    # seed_tickets(session, users, num_tickets_per_user)

    # Modified to randomly give each user between 0 and 5 tickets:
    seed_tickets(session, users)
    tickets = session.query(Ticket).all()

    #Create the technicians:
    num_technicians = 3
    seed_technicians(session, users, num_technicians)
    technicians = session.query(Technician).all()

    #Create the ticket lines:
    num_ticket_lines_per_ticket = 3
    seed_ticket_lines(session, num_ticket_lines_per_ticket, tickets, technicians)
    ticketlines = session.query(TicketLine).all()

def reset_department_names():
    department_names = [
        "IT Support",
        "Customer Service",
        "Marketing",
        "Finance",
        "Human Resources",
        "Sales",
        "Research and Development",
        "Legal",
        "Facilities Management",
        "Quality Assurance",
        "Product Management",
        "Supply Chain",
        "Administration",
        "Engineering",
        "Public Relations"
    ]

    departments = session.query(Department).all()

    for department in departments:
        selected_department = fake.random_int(min=0, max=len(department_names)-1)
        department.name = department_names[selected_department]
    session.commit()

def reset_organization_names():
    organization_names = [
        "Acme Corporation",
        "Tech Solutions Inc.",
        "Global Enterprises",
        "Marketing Innovators",
        "Finance World Group"
    ]

    organizations = session.query(Organization).all()

    for organizations in organizations:
        selected_organization = fake.random_int(min=0, max=len(organization_names)-1)
        organizations.name = organization_names[selected_organization]
    session.commit()


# import pandas as pd

# date_time_pre=fake.date_time_this_decade()

# hours_taken = fake.random_int(min=0, max=4)
# minutes_taken = fake.random_int(min=0, max=59)

# date_time_post = date_time_pre + pd.DateOffset(hours=hours_taken, minutes=minutes_taken)


# print(date_time_pre)
# print(hours_taken)

# print(minutes_taken)
# print(date_time_post)