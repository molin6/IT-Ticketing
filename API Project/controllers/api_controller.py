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

@app.post("/Tickets")
def create_ticket():
    '''
    Creates a new ticket
    '''
    ticket_data = request.get_json()
    new_ticket = Ticket.create_ticket(ticket_data)
    return jsonify(new_ticket.as_dict())

@app.put("/Tickets/<ticket_id>")
def update_ticket(ticket_id):
    '''
    Updates a ticket based on the ticket id
    '''
    ticket_data = request.get_json()
    working = Ticket.update_ticket(ticket_id, ticket_data)

    if working is not None:
        return jsonify(working.as_dict())
    else:
        return 'Ticket not updated'

@app.get("/Users")
def read_users_10():
    '''
    Returns # of records in the User table based on the optional parameter
    '''
    limit = request.args.get('limit', default=10, type=int)
    users = User.read_users_10()[:limit]
    return jsonify(users)

@app.delete("/Users/<user_id>")
def delete_user(user_id):
    '''
    Deletes a user based on the user id
    '''
    working = User.delete_user(user_id)

    if working:
        return 'User deleted Successfully!'
    else:
        return 'User not deleted'

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

