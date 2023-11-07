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

def get_int_arg(request, arg_name, default_value=None, non_negative=False):
    '''
    Gets an integer argument from the request object

    params: request - the request object
            arg_name - the name of the argument to retrieve
            default_value - the default value to use if the argument is not provided
            non_negative - whether to check if the value is non-negative
    '''

    arg_value = request.args.get(arg_name, default_value)
    if arg_value is None:
        return None, jsonify({'Error': f'Missing {arg_name} parameter'}), 400

    try:
        arg_value = int(arg_value)
    except ValueError:
        return None, jsonify({'Error': f'Invalid {arg_name} value'}), 400

    if non_negative and arg_value < 0:
        return None, jsonify({'Error': f'{arg_name} must be non-negative'}), 400

    return arg_value, None, None

def check_technician_exists(technician_id):
    '''
    Checks if a technician exists in the database

    params: technician_id - the id of the technician to check
    '''
    technician = Technician.select_technician_by_id(technician_id)
    if technician is None:
        return False
    else:
        return True


#Technician GET Calls
@app.get("/Technicians")
def select_technicians():
    '''
    Returns all technicians from the database

    params: limit - optional parameter to limit the number of results returned, default is 10
    '''

    limit, error, status = get_int_arg(request, 'limit', 10, True)
    if error:
        return error, status
    

    # try:
    #     limit = int(request.args.get('limit', 10))
    # except ValueError:
    #     # Return an error response
    #     return jsonify({'error': 'Invalid limit value'}), 400

    technicians = Technician.select_technicians(limit)
    return jsonify(technicians), 200
@app.get("/Technicians/Names")
def read_technician_names():
    '''
    Returns the first and last names of all the technicians
    '''
    technician_names = Technician.read_technician_names()
    return jsonify(technician_names), 200
@app.get("/Technicians/AvgTicketTimes")
def read_technician_avg_ticket_times():
    '''
    Retrieve and print the average ticket times for each technician.
    '''
    return jsonify(Technician.read_technician_avg_ticket_times()), 200
@app.get("/Technicians/TicketsInfo")
def read_technician_ticketinfo():
    '''
    Retrieves ticket information for each technician based on technician Id.
    '''

    technician_id, error, status = get_int_arg(request, 'technician_id')
    if error:
        return error, status

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

    technician_id, error, status = get_int_arg(request, 'technician_id')
    if error:
        return error, status

    manager = Technician.get_technicians_manager(technician_id)

    if manager is not None:
        return jsonify(manager), 200
    else:
        return f"Error: Technician with technician_id {technician_id} either does not exist, or their manager does not exist", 404


    






#Technician POST Calls
@app.post("/Technicians")
def update_technician_manager():
    '''
    Updates the manager of a technician

    params: technician_id - the id of the technician whose manager is getting updated
            manager_user_id - the user id of the new manager
    '''
    technician_id, error, status = get_int_arg(request, 'technician_id')
    if error:
        return error, status

    manager_user_id, error, status = get_int_arg(request, 'manager_user_id')
    if error:
        return error, status

    update = Technician.update_technician_manager(technician_id=technician_id, manager_user_id=manager_user_id)

    if update is not None:
        return jsonify(update), 200
    else:
        return f"Error: Provided technician_id or manager_user_id value does not exist", 404

#TicketLine GET Calls
@app.get("/TicketLines")
def read_ticket_lines():
    '''
    Returns # of records in the Ticket Line table based on the optional parameter

    params: limit - optional parameter to limit the number of results returned, default is 10
    '''

    limit, error, status = get_int_arg(request, 'limit', 10, True)
    if error:
        return error, status

    ticket_lines = TicketLine.read_ticket_lines()[:limit]
    return jsonify(ticket_lines), 200

#Ticket GET Calls
@app.get("/Tickets")
def read_tickets():
    '''
    Returns ticket records from the Ticket table

    params: limit - optional parameter to limit the number of results returned, default is 10
    '''
    limit, error, status = get_int_arg(request, 'limit', 10, True)
    if error:
        return error, status
    
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

    ticket_id, error, status = get_int_arg(request, 'ticket_id')
    if error:
        return error, status

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
    limit, error, status = get_int_arg(request, 'limit', 10, True)
    if error:
        return error, status

    users = User.read_users()[:limit]
    return jsonify(users), 200

@app.get("/Users/TicketCounts")
def read_user_ticket_counts():
    '''
    TODO: Insert tooltip documentation here
    params: user_id - optional parameter for the id of the user to retrieve the ticket count information
    '''


    user_id, error, status = get_int_arg(request, 'user_id')
    if error:
        return error, status

    users = User.read_user_ticket_counts(user_id)
    return jsonify(users), 200

#User DELETE Calls
@app.delete("/Users")
def delete_user():
    '''
    Deletes a user based on the user id

    params: user_id - the id of the user to delete, contained in the URL
    '''

    user_id, error, status = get_int_arg(request, 'user_id')
    if error:
        return error, status

    result = User.delete_user(user_id)

    if isinstance(result, dict):
        # An error occurred, return the error message and status code
        return jsonify(result), result.get('status', 500)
    else:
        return 'User deleted Successfully!', 200

#Organization GET Calls
@app.get("/Organizations")
def read_organizations():
    '''
    Returns # of records in the Organization table based on the optional parameter

    params: limit - optional parameter to limit the number of results returned, default is 10
    '''
    limit, error, status = get_int_arg(request, 'limit', 10, True)
    if error:
        return error, status

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
    limit, error, status = get_int_arg(request, 'limit', 10, True)
    if error:
        return error, status

    departments = Department.read_departments()[:limit]
    return jsonify(departments), 200


@app.get("/Departments/AvgResolutionTimes")
def read_department_avg_resolution_time():
    '''
    Retrieve and print the average resolution times for each department.
    '''
    return jsonify(Department.read_department_avg_resolution_time()), 200
