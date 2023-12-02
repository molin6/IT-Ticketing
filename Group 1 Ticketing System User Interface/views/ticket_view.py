import requests
import json
from datetime import datetime
# import datetime
from utils import text_print_utils as utils
from utils.text_print_options import PrintOptions, Term

def create_ticket(print_options):
    options = print_options
    userid = int(input("Enter the ID of the user who created the ticket: "))
    departmentid = int(input("Enter the ID of the department: "))
    priorticketid = int(input("Enter the ID of the prior ticket (enter 0 for no prior ticket): "))
    if priorticketid == 0:
        priorticketid = None
    else:
        priorticketid = priorticketid
    ticketcategory = input("Enter the category of the ticket: ")
    subject = input("Enter the subject of the ticket: ")
    description = input("Enter the description of the ticket: ")

    # Automatically add the current date and time for the created_at field
    open_date_time = datetime.now().isoformat()
    status = "Active"

    ticket_data = {
        "user_id": userid,
        "department_id": departmentid,
        "prior_ticket_id": priorticketid,
        "ticket_category": ticketcategory,
        "open_date_time": open_date_time,
        "status": status,
        "description": description,
        "subject": subject
    }

    response = requests.post(f"{api_url_base}/Tickets", json=ticket_data)

    if response.status_code == 200:
        options.text_color = Term.BLUE_BOLD
        utils.print_divider(options=options)
        utils.print_text_block("Message", top_border=False, bottom_border=False, options=options)
        utils.print_text("Ticket created successfully.", options=options)
        utils.print_divider(options=options)
        utils.print_text("Created Ticket Details:", options=options) 
        result = json.dumps(response.json(), indent=2)
        utils.print_text(result, options=options)
        utils.print_blank_line(options=options)
        utils.print_divider(options=options)
    else:
        options.text_color = Term.BLUE_BOLD
        utils.print_divider(options=options)
        utils.print_text_block("Message", top_border=False, bottom_border=False, options=options)
        utils.print_text("Ticket creation failed.", options=options)
        utils.print_text(response.text, options=options)

def delete_ticket(ticket_id):
    url = f"{api_url_base}/Tickets?ticket_id={ticket_id}"
    response = requests.delete(url)
    return response.text

def remove_ticket(print_options):
    options = print_options
    ticket_id = input("Enter the Ticket ID to delete: ")
    result = delete_ticket(ticket_id)
    options.text_color = Term.BLUE_BOLD
    utils.print_divider(options=options)
    utils.print_text_block("Message", top_border=False, bottom_border=False, options=options)
    utils.print_text(result, options=options)
    utils.print_blank_line(options=options)
    utils.print_divider(options=options)

def put_ticket(ticket_id, ticket_data):

    ticket_data.pop("open_date_time", None)
    ticket_data.pop("close_date_time", None)
    ticket_data.pop("status", None)

    url = f"{api_url_base}/Tickets?ticket_id={ticket_id}"
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, data=json.dumps(ticket_data), headers=headers)
    return response.text

def modify_ticket(print_options):
    options = print_options
    ticket_id = input("Enter the Ticket ID to view and modify: ")

    ticket_info = view_one_ticket(ticket_id,print_options=print_options)

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

        options.text_color = Term.BLUE_BOLD
        utils.print_divider(options=options)

        utils.print_text_block("Message", top_border=False, bottom_border=False, options=options)
        result = put_ticket(ticket_id, ticket_data)
        utils.print_text(result, options=options)
        utils.print_blank_line(options=options)
        utils.print_divider(options=options)
        
    else:
        print("Ticket not modified.")
        # break

def view_one_ticket(ticket_id, print_options):
    options = print_options
    url = f"{api_url_base}/Tickets/ID?ticket_id={ticket_id}"
    params = {}
    data = {}
    response = requests.get(url, params=params, data=data)

    if response.status_code == 200:
        aticket = response.json()
        if len(aticket) == 0:
            print("No ticket found.")
        else:
            options.text_color = Term.BLUE_BOLD
            utils.print_divider(options=options)

            utils.print_text_block(f"Ticket #{ticket_id}", top_border=False, bottom_border=False, options=options)

            utils.print_json_in_table_format(aticket, options=options)
            utils.print_blank_line(options=options)
            utils.print_divider(options=options)
    else:
        print(f"{response.json()}; Error code: {response.status_code}")
    options.text_color = Term.GREEN

def get_all_tickets():
    url = f"{api_url_base}/Tickets/All"
    response = requests.get(url)
    return response.json()

def view_all_tickets(print_options):
    options = print_options

    while True:
        utils.print_text_block("How many tickets would you like to view at a time? Please enter a whole number, or type 'all' to view all tickets.", bottom_border = False, options=options)
        utils.print_divider(options=options)
        user_input = input("Enter a command: ")

        if user_input == "all":
            tickets = get_all_tickets()
            
            if len(tickets) == 0:
                        print("No ticket found.")
                        break
            else:
                options.text_color = Term.BLUE_BOLD
                utils.print_divider(options=options)

                utils.print_text_block("Current Technicians", top_border=False, bottom_border=False, options=options)
                ticket_dict = {}
                for ticket in tickets:

                    key = f"Ticket {ticket['Ticket ID']}"
                    ticket_dict[key] = f"{ticket['Subject']} {ticket['Description']} {ticket['Status']} {ticket['Open Date Time']} {ticket['Close Date Time']} {ticket['Ticket Category']} {ticket['Prior Ticket ID']} {ticket['Department ID']} {ticket['User ID']}"

                utils.print_json_in_table_format(ticket_dict, options=options)
                utils.print_blank_line(options=options)
                utils.print_divider(options=options)

                break    
        else:
            start = 0
            limit = int(user_input)
            tickets = customize_view_all_tickets(start, limit)
            if len(tickets) == 0:
                print("No ticket found.")
                break
            else:
                options.text_color = Term.BLUE_BOLD
                utils.print_divider(options=options)

                utils.print_text_block("Tickets", top_border=False, bottom_border=False, options=options)
                ticket_dict = {}
                for ticket in tickets:

                    key = f"Ticket {ticket['Ticket ID']}"
                    ticket_dict[key] = f"{ticket['Subject']} {ticket['Description']} {ticket['Status']} {ticket['Open Date Time']} {ticket['Close Date Time']} {ticket['Ticket Category']} {ticket['Prior Ticket ID']} {ticket['Department ID']} {ticket['User ID']}"

                utils.print_json_in_table_format(ticket_dict, options=options)
                utils.print_blank_line(options=options)
                utils.print_divider(options=options)
            
            while True:
                utils.print_text_block("Would you like to view more tickets? Please enter 'yes' or 'no'.", bottom_border = False, options=options)
                utils.print_divider(options=options)
                user_input = input("Enter a command: ")
                if user_input == "yes":
                    start += limit
                    tickets = customize_view_all_tickets(start, limit)
                    options.text_color = Term.BLUE_BOLD
                    utils.print_divider(options=options)

                    utils.print_text_block("Tickets", top_border=False, bottom_border=False, options=options)
                    ticket_dict = {}
                    for ticket in tickets:

                        key = f"Ticket {ticket['Ticket ID']}"
                        ticket_dict[key] = f"{ticket['Subject']} {ticket['Description']} {ticket['Status']} {ticket['Open Date Time']} {ticket['Close Date Time']} {ticket['Ticket Category']} {ticket['Prior Ticket ID']} {ticket['Department ID']} {ticket['User ID']}"

                    utils.print_json_in_table_format(ticket_dict, options=options)
                    utils.print_blank_line(options=options)
                    utils.print_divider(options=options)
                elif user_input == "no":
                    break
                else:
                    print("Invalid input. Please try again.")
                    break
            break
    options.text_color = Term.GREEN

def customize_view_all_tickets(start, limit):
        
        url = f"{api_url_base}/Tickets"

        params = {'start': start, 'limit': limit}

        response = requests.get(url, params=params)
        return response.json()


        # # Get the next batch of tickets
        # url = f"{api_url_base}/Tickets?limit={limit}&offset={offset}"
        # response = requests.get(url)
        # tickets = response.json()

        # if not tickets:
        #     print("No more tickets to display.")
        #     break

        # print("Tickets:")
        # for ticket in tickets:
        #     print(json.dumps(ticket, indent=2))

        # offset += limit

        # show_more = input("Do you want to view more tickets? (yes/no): ").lower()
        # if show_more != "yes":
        #     break

def view_ticket(print_options):
    view_choice = input("Do you want to view one ticket or all tickets? (one/more): ").lower()

    if view_choice == "one":
        ticket_id = input("Enter the Ticket ID to view: ")
        ticket_info = view_one_ticket(ticket_id, print_options=print_options)
        print(json.dumps(ticket_info, indent=2))
    elif view_choice == "more":
        view_all_tickets(print_options=print_options)
    else:
        print("Invalid choice. Please enter 'one' or 'more'.")


def run(base_url):
    global api_url_base
    api_url_base = base_url

    print_options = PrintOptions(border_marker_color=Term.GREEN, line_divider_color=Term.GREEN, text_color=Term.GREEN)
    utils.print_text_block("Ticket Management System", bottom_border = False)

    menu_options = ["1. Create a Ticket", "2. Delete a Ticket", "3. Modify a Ticket", "4. View a Ticket/Tickets", "0. Main Menu"]
    quit = False
    while not quit:
        utils.print_text_block("Menu Options:", menu_options)
        user_input = input("Enter a command: ")

        if user_input == "1":
            create_ticket(print_options)
        elif user_input == "2":
            remove_ticket(print_options)
        elif user_input == "3":
            modify_ticket(print_options)
        elif user_input == "4":
            view_ticket(print_options)
        elif user_input == "0":
            print("Exiting Ticket Management System.")
            quit = True
        else:
            print("Invalid command. Please try again.")
