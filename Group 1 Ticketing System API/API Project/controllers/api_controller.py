from models.department_model import Department
from models.organization_model import Organization
from models.technician_model import Technician
from models.ticket_line_model import TicketLine
from models.ticket_model import Ticket
from models.user_model import User
from flask import Flask, jsonify, request

app = Flask(__name__)

def run():
    # Start the API server
    app.run(debug=True)

@app.route('/')
def hello_world():
    return 'Hello world'

#Technician GET Calls
@app.get("/Technicians")
def select_technicians():
    '''
    Returns all technicians from the database

    params: limit - optional parameter to limit the number of results returned, default is 10
    '''
    try:
        limit = int(request.args.get('limit', 10))
    except ValueError:
        # Return an error response
        return jsonify({'error': 'Invalid limit value'}), 400

    technicians = Technician.select_technicians(limit)
    return jsonify(technicians), 200
@app.get("/Technicians/Names")
def read_technician_names():
    '''
    Returns the first and last names of all the technicians
    '''

    technician_names = Technician.read_technician_names()
    return technician_names
@app.get("/Technicians/AvgTicketTimes")
def read_technician_avg_ticket_times():
    '''
    Retrieve and print the average ticket times for each technician.
    '''
    return Technician.read_technician_avg_ticket_times()
@app.get("/Technicians/TicketsInfo")
def read_technician_ticketinfo():#Use for an example on how to return error messages
    '''
    Retrieve and print ticket information for each technician based on technician ID.
    '''
    try:
        technician_id = int(request.args.get('technician_id'))
    except ValueError:
        # Return an error response
        return jsonify({'error': 'Invalid technician_id value'}), 400

    ticket_info = Technician.read_technician_ticketinfo(technician_id)

    if ticket_info is not None:
        return jsonify(ticket_info), 200
    else:
        return f"Error: Technician doesn't exist for technician_id {technician_id}", 404
@app.get("/Technicians/Manager")
def get_technicians_manager():
    '''
    Retrieve the manager of a technician

    params: technician_id - the id of the technician whose manager is getting retrieved
    '''
    try:
        technician_id = int(request.args.get('technician_id'))
    except ValueError:
        return jsonify({'Error': 'Invalid technician_id value'}), 400

    manager = Technician.get_technicians_manager(technician_id)

    if manager is not None:
        return jsonify(manager), 200
    else:
        return f"Error: Technician with technician_id {technician_id} either does not exist, or their manager does not exist", 404

#Technician POST Calls
@app.post("/Technicians")
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
        return jsonify({'Error': 'Invalid technician_id or manager_id value'}), 400

    update = Technician.update_technician_manager(technician_id=technician_id, manager_id=manager_id)

    if update is not None:
        return jsonify(update), 200
    else:
        return f"Error: Provided technician_id or manager_id value does not exist", 404

#TicketLine GET Calls
@app.get("/TicketLines")
def read_ticket_lines():
    '''
    Returns # of records in the Ticket Line table based on the optional parameter

    params: limit - optional parameter to limit the number of results returned, default is 10
    '''
    try:
        limit = request.args.get('limit', default=10, type=int)
    except ValueError:
        return jsonify({'error': 'Invalid limit value'}), 400
    ticket_lines = TicketLine.read_ticket_lines()[:limit]
    return jsonify(ticket_lines), 200

#Ticket GET Calls
@app.get("/Tickets")
def read_tickets():
    '''
    Returns # of records in the Ticket table based on the optional parameter

    params: limit - optional parameter to limit the number of results returned, default is 10
    '''
    try:
        limit = request.args.get('limit', default=10, type=int)
    except ValueError:
        return jsonify({'error': 'Invalid limit value'}), 400
    
    tickets = Ticket.read_tickets()[:limit]
    return jsonify(tickets), 200


#Ticket POST Calls
@app.post("/Tickets")
def create_ticket():
    '''
    Creates a ticket based on the contents of the request body.
    Set the request body to a JSON object containing the data for the new ticket.

    The JSON object should have the following keys:

    title: The title of the ticket (string).
    description: The description of the ticket (string).
    status: The status of the ticket (string).
    priority: The priority of the ticket (string).
    created_by: The ID of the user who created the ticket (integer).
    assigned_to: The ID of the user who the ticket is assigned to (integer).

    example:
    {
        "title": "New ticket",
        "description": "This is a new ticket",
        "status": "Open",
        "priority": "High",
        "created_by": 1,
        "assigned_to": 2
    }
    '''
    ticket_data = request.get_json()
    new_ticket = Ticket.create_ticket(ticket_data)
    return 'Successfully added a new ticket', 200
    #return jsonify(new_ticket.as_dict()), 200

#Ticket PUT Calls
@app.put("/Tickets")
def update_ticket():
    '''
    Updates a ticket based on the ticket id, according to the contents of the request body.
    Set the request body to a JSON object containing the data for the updated ticket.

    params: ticket_id - the id of the ticket which is getting updated

    body: The JSON object containing the data for the updated ticket.
        The JSON object should have the following keys:

        title: The updated title of the ticket (string).
        description: The updated description of the ticket (string).
        status: The updated status of the ticket (string).
        priority: The updated priority of the ticket (string).
        created_by: The updated ID of the user who created the ticket (integer).
        assigned_to: The updated ID of the user who the ticket is assigned to (integer).

        example:
        {
            "title": "Updated ticket",
            "description": "This ticket has been updated",
            "status": "Closed",
            "priority": "Low",
            "created_by": 1,
            "assigned_to": 2
        }

    '''
    ticket_data = request.get_json()

    try:
        ticket_id = int(request.args.get('ticket_id'))
    except ValueError:
        # Return an error response
        return jsonify({'error': 'Invalid ticket_id value'}), 400

    working = Ticket.update_ticket(ticket_id, ticket_data)

    if working is not None:
        return 'Successfully updated the ticket', 200
    else:
        return 'Ticket is not updated', 500

#User GET Calls
@app.get("/Users")
def read_users():
    '''
    Returns # of records in the User table based on the optional parameter

    params: limit - optional parameter to limit the number of results returned, default is 10
    '''
    try:
        limit = request.args.get('limit', default=10, type=int)
    except ValueError:
        jsonify({'error': 'Invalid user_id value'}), 400

    users = User.read_users()[:limit]
    return jsonify(users), 200

@app.get("/Users/TicketCounts")
def read_user_ticket_counts():
    '''
    TODO: Insert tooltip documentation here
    params: user_id - optional parameter for the id of the user to retrieve the ticket count information
    '''
    try:
        user_id_value = request.args.get('user_id')
        if user_id_value is not None:
            user_id = int(request.args.get('user_id'))
        else:
            user_id = None
    except ValueError:
        # Return an error response
        return jsonify({'error': 'Invalid user_id value'}), 400

    users = User.read_user_ticket_counts(user_id)
    return jsonify(users), 200

#User DELETE Calls
@app.delete("/Users")
def delete_user():
    '''
    Deletes a user based on the user id

    params: user_id - the id of the user to delete, contained in the URL
    '''
    try:
        user_id = int(request.args.get('user_id'))
    except ValueError:
        # Return an error response
        return jsonify({'error': 'Invalid user_id value'}), 400

    working = User.delete_user(user_id)

    if working:
        return 'User deleted Successfully!', 200
    else:
        return 'User not deleted', 500

#Organization GET Calls
@app.get("/Organizations")
def read_organizations():
    '''
    Returns # of records in the Organization table based on the optional parameter

    params: limit - optional parameter to limit the number of results returned, default is 10
    '''
    try:
        limit = request.args.get('limit', default=10, type=int)
    except ValueError:
        return jsonify({'error': 'Invalid limit value'}), 400
    organizations = Organization.read_organizations()[:limit]
    return jsonify(organizations), 200



@app.get("/Organizations/TicketCounts")
def read_organizations_tickets_count():
    '''
    Retrieve ticket counts for each organization.
    '''
    return jsonify(Organization.read_organizations_tickets_count()), 200

#Department GET Calls
@app.get("/Departments")
def read_departments():
    '''
    Returns # of records in the Department table based on the optional parameter

    params: limit - optional parameter to limit the number of results returned, default is 10
    '''
    try:
        limit = request.args.get('limit', default=10, type=int)
    except ValueError:
        return jsonify({'error': 'Invalid limit value'}), 400
    departments = Department.read_departments()[:limit]
    return jsonify(departments), 200


@app.get("/Departments/AvgResolutionTimes")
def read_department_avg_resolution_time():
    '''
    Retrieve and print the average resolution times for each department.
    '''
    return jsonify(Department.read_department_avg_resolution_time()), 200
