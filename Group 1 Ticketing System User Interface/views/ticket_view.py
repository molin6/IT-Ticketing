import requests
import json
from datetime import datetime
# import datetime
from utils import text_print_utils as utils
from utils.text_print_options import PrintOptions, Term

def create_ticket():
    userid = int(input("Enter the ID of the user who created the ticket: "))
    departmentid = int(input("Enter the ID of the department: "))
    priorticketid = int(input("Enter the ID of the prior ticket: "))
    ticketcategory = input("Enter the category of the ticket: ")
    subject = input("Enter the subject of the ticket: ")
    description = input("Enter the description of the ticket: ")

    # Automatically add the current date and time for the created_at field
    open_date_time = datetime.now().isoformat()
    close_date_time = None
    status = "Open"

    ticket_data = {
        "user_id": userid,
        "department_id": departmentid,
        "prior_ticket_id": priorticketid,
        "ticket_category": ticketcategory,
        "open_date_time": open_date_time,
        "close_date_time": close_date_time,
        "status": status,
        "description": description,
        "subject": subject
    }

    response = requests.post(f"{api_url_base}/Tickets", json=ticket_data)

    if response.status_code == 200:
        print("Ticket created successfully.")
        print("Created Ticket Details:")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Failed to create ticket. Status code: {response.status_code}")
        print(response.text)


def delete_ticket():
    ticket_id = input("Enter the Ticket ID to delete: ")
    url = f"{api_url_base}/Tickets?ticket_id={ticket_id}"
    response = requests.delete(url)
    print(response.text)

def modify_ticket(ticket_id, ticket_data):

    ticket_data.pop("open_date_time", None)
    ticket_data.pop("close_date_time", None)
    ticket_data.pop("status", None)

    url = f"{api_url_base}/Tickets?ticket_id={ticket_id}"
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, data=json.dumps(ticket_data), headers=headers)
    return response.text

def modify_ticket():
    ticket_id = input("Enter the Ticket ID to view and modify: ")

    ticket_info = view_ticket(ticket_id)

    print("Ticket Details:")
    print(json.dumps(ticket_info, indent=2))

    modify_choice = input("Do you want to modify this ticket? (yes/no): ").lower()
    if modify_choice == "yes":
        ticket_data = {
            "user_id": int(input("Enter User ID: ")),
            "department_id": int(input("Enter Department ID: ")),
            "prior_ticket_id": int(input("Enter Prior Ticket ID: ")),
            "ticket_category": input("Enter Ticket Category: "),
            "description": input("Enter Description: "),
            "subject": input("Enter Subject: ")
        }

        result = modify_ticket(ticket_id, ticket_data)

        print(result)
        if "Successfully updated the ticket" in result:
            print("Ticket updated successfully!")
        else:
            print("Failed to update the ticket.")
            # break  # Exit the loop after modifying the ticket
    else:
        print("Ticket not modified.")
        # break

def view_ticket(ticket_id):
    url = f"{api_url_base}/Tickets?ticket_id={ticket_id}"
    response = requests.get(url)
    return response.json()

def view_all_tickets():
    limit = 10
    offset = 0

    while True:
        # Get the next batch of tickets
        url = f"{api_url_base}/Tickets?limit={limit}&offset={offset}"
        response = requests.get(url)
        tickets = response.json()

        if not tickets:
            print("No more tickets to display.")
            break

        print("Tickets:")
        for ticket in tickets:
            print(json.dumps(ticket, indent=2))

        offset += limit

        show_more = input("Do you want to view more tickets? (yes/no): ").lower()
        if show_more != "yes":
            break

def view_ticket():
    view_choice = input("Do you want to view one ticket or all tickets? (one/all): ").lower()

    if view_choice == "one":
        ticket_id = input("Enter the Ticket ID to view: ")


        view_ticket(ticket_id)


        print(json.dumps(ticket_info, indent=2))
    elif view_choice == "all":
        view_all_tickets()
    else:
        print("Invalid choice. Please enter 'one' or 'all'.")


def run(base_url):
    global api_url_base
    api_url_base = base_url
    utils.print_text_block("Ticket Management System", bottom_border = False)

    menu_options = ["1. Create a Ticket", "2. Delete a Ticket", "3. Modify a Ticket", "4. View a Ticket/Tickets", "0. Quit"]
    quit = False
    while not quit:
        utils.print_text_block("Menu Options:", menu_options)
        user_input = input("Enter a command: ")

        if user_input == "1":
            create_ticket()
        elif user_input == "2":
            delete_ticket()
        elif user_input == "3":
            modify_ticket()
        elif user_input == "4":
            view_ticket()
        elif user_input == "0":
            print("Exiting Ticket Management System.")
            quit = True
        else:
            print("Invalid command. Please try again.")
