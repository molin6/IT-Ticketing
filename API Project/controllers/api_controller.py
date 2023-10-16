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
from views import technician_view
from views import api_view

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

#Technician GET Calls

@app.get("/Technicians/")
def select_technicians():
    '''
    Returns all technicians from the database
    '''

    limit = int(request.args.get('limit',10))

    technicians = Technician.select_technicians(limit)
    return jsonify(technicians)


@app.get("/Technicians/Names/")
def read_technician_names():
    '''
    Returns the first and last names of all the technicians
    '''

    technician_names = Technician.read_technician_names()
    return technician_names

@app.get("/Technicians/AvgTicketTimes/")
def read_technician_avg_ticket_times():
    '''
    Retrieve and print the average ticket times for each technician.
    '''
    return Technician.read_technician_avg_ticket_times()

@app.get("/Technicians/TicketsInfo")
def read_technician_ticketinfo():
    '''
    Retrieve and print ticket information for each technician based on technician ID.
    '''
    return Technician.read_technician_ticketinfo()


@app.get("/Technicians/Manager/")
def get_technicians_manager():
    '''
    Retrieve the manager of a technician

    params: technician_id - the id of the technician whose manager is getting retrieved
    '''
    try:
        technician_id = int(request.args.get('technician_id'))
    except ValueError:
        # Return an error response
        return jsonify({'error': 'Invalid technician_id value'}), 400

    manager = Technician.get_technicians_manager(technician_id=technician_id)

    return jsonify(manager)


#Technician POST Calls

@app.post("/Technicians/Update/")
def update_technician_manager():
    '''
    Update the manager of a technician

    params: technician_id - the id of the technician whose manager is getting updated
            manager_id - the user id of the new manager
    '''
    try:
        technician_id = int(request.args.get('technician_id'))
        manager_id = int(request.args.get('manager_id'))
    except ValueError:
        # Return an error response
        return jsonify({'error': 'Invalid technician_id or manager_id value'}), 400

    update = Technician.update_technician_manager(technician_id=technician_id, manager_id=manager_id)

    return jsonify(update)





#User Calls

@app.get("/Users/TicketCounts/")
def read_user_ticket_counts(user_id=None):
    '''
    TODO: Insert tooltip documentation here
    '''
    return User.read_user_ticket_counts(user_id=None)

#Department Calls

@app.get("/Departments/AvgResolutionTimes")
def read_department_avg_resolution_time():
    '''
    Retrieve and print the average resolution times for each department.
    '''
    return Department.read_department_avg_resolution_time()

#Organization Calls

@app.get("/Organizations/TicketCounts")
def read_organizations_tickets_count():
    '''
    Retrieve ticket counts for each organization.
    '''
    return Organization.read_organizations_tickets_count()

