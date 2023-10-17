from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, joinedload
from datetime import timedelta
from models.department_model import Department
from models.organization_model import Organization
from models.technician_model import Technician
from models.ticket_line_model import TicketLine
from models.ticket_model import Ticket
from models.user_model import User
from models.base_model import Base

# FastAPI setup
# app = FastAPI(
#     title="IT Ticketing System API",
#     description="API for Group 1's IT Ticketing System",
#     version="0.1",
# )

from flask import Flask, jsonify, request

app = Flask(__name__)

def run():
    # Start the API server
    app.run(debug=True)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.get("/Technicians/")
def read_technician_names():
    '''
    Returns the first and last names of all the technicians
    '''
    return Technician.read_technician_names()

@app.get("/Ticketlines")
def read_ticket_lines_10():
    '''
    Returns # of records in the Ticket Line table based on the optional parameter
    '''
    limit = request.args.get('limit', default=10, type=int)
    ticket_lines = TicketLine.read_ticket_lines_10()[:limit]
    return jsonify(ticket_lines)

@app.get("/Tickets")
def read_tickets_10():
    '''
    Returns # of records in the Ticket table based on the optional parameter
    '''
    limit = request.args.get('limit', default=10, type=int)
    tickets = Ticket.read_tickets_10()[:limit]
    return jsonify(tickets)

@app.get("/Users")
def read_users_10():
    '''
    Returns # of records in the User table based on the optional parameter
    '''
    limit = request.args.get('limit', default=10, type=int)
    users = User.read_users_10()[:limit]
    return jsonify(users)

@app.get("/Organizations")
def read_organizations_10():
    '''
    Returns # of records in the Organization table based on the optional parameter
    '''
    limit = request.args.get('limit', default=10, type=int)
    organizations = Organization.read_organizations_10()[:limit]
    return jsonify(organizations)

@app.get("/Departments")
def read_departments_10():
    '''
    Returns # of records in the Department table based on the optional parameter
    '''
    limit = request.args.get('limit', default=10, type=int)
    departments = Department.read_departments_10()[:limit]
    return jsonify(departments)

@app.get("/Technicians/AvgTicketTimes/")
def read_technician_avg_ticket_times():
    '''
    TODO: Insert tooltip documentation here
    '''
    return Technician.read_technician_avg_ticket_times()

@app.get("/Users/TicketCounts/")
def read_user_ticket_counts(user_id=None):
    '''
    TODO: Insert tooltip documentation here
    '''
    return User.read_user_ticket_counts(user_id=None)

@app.get("/Departments/AvgResolutionTimes")
def read_department_avg_resolution_time():
    '''
    Retrieve and print the average resolution times for each department.
    '''
    return Department.read_department_avg_resolution_time()

@app.get("/Technicians/TicketsInfo")
def read_technician_ticketinfo():
    '''
    Retrieve and print ticket information for each technician based on technician ID.
    '''
    return Technician.read_technician_ticketinfo()

@app.get("/Organizations/TicketCounts")
def read_organizations_tickets_count():
    '''
    Retrieve ticket counts for each organization.
    '''
    return Organization.read_organizations_tickets_count()

