import requests
import json
import textwrap
from datetime import datetime
from utils import text_print_utils as utils
from utils.text_print_options import PrintOptions, Term

def display_technician_information(print_options):
    options = print_options
    start = 0
    limit = None

    while True:

        utils.print_text_block(text="How many technicians would you like to view at a time? Please enter a whole number, or type 'all' to view all technicians.", bottom_border = False, options=options)
        utils.print_divider(options=options)
        user_input = utils.get_input("Enter a command: ")
        if user_input == "all":
            limit = None
            break
        else:
            try:
                limit = int(user_input)
                break
            except:
                print("Invalid input. Please try again.")


    url = f"{api_url_base}Technicians"

    get_more = True
    while get_more:
        params = {'start': start, 'limit': limit}
        data = {}
        response = requests.get(url, params=params, data=data)

        if response.status_code == 200:
            technicians = response.json()
            if len(technicians) == 0:
                print("No technicians found.")
                break
            utils.print_divider(options=options)

            for technician in technicians:

                options.alignment = 'center'
                utils.print_text(f"Displaying Technician: {technician['technician_user_data']['first_name']} {technician['technician_user_data']['last_name']}", options)

                options.line_divider_char = '-'
                utils.print_divider(options=options)

                utils.print_blank_line(options=options)

                ordered_keys = ['technician_id', 'technician_user_id', 'manager_user_id']
                rename_keys = {'technician_id': 'Technician Id', 'technician_user_id': 'Technician User Id', 'manager_user_id': 'Technician\'s Manager\'s Id'}

                options.tab_spaces = 0
                options.alignment = 'left'
                utils.print_json_in_table_format(technician, ordered_keys, rename_keys, options=options)

                ordered_keys = ['first_name', 'last_name', 'title', 'email_address', 'phone_number', 'organization_id']
                rename_keys = {'first_name': 'First Name'
                                , 'last_name': 'Last Name'
                                , 'title': 'Title'
                                , 'email_address': 'Email Address'
                                , 'phone_number': 'Phone #'
                                , 'organization_id': 'Organization Id'
                            }

                options.tab_spaces = 1
                utils.print_json_in_table_format(technician['technician_user_data'], ordered_keys, rename_keys, options=options)

                options.tab_spaces = 0
                utils.print_blank_line(options=options)
                utils.print_divider(options=options)

        else:
            print(f"{response.json()}; Error code: {response.status_code}")
            break

        if limit is None:
            break
        start += limit

        while True:
            options.alignment = 'center'
            utils.print_text_block(text="Would you like to view more technicians? Please enter 'yes' or 'no'.", bottom_border = False, options=options)
            utils.print_divider(options=options)
            user_input = utils.get_input("Enter a command: ")
            if user_input == "yes":
                get_more = True
                break
            elif user_input == "no":
                get_more = False
                break
            else:
                print("Invalid input. Please try again.")

def display_technician_names(print_options):
    options = print_options
    url = f"{api_url_base}Technicians/Names"
    params = {}
    data = {}
    response = requests.get(url, params=params, data=data)

    if response.status_code == 200:
        technicians = response.json()
        if len(technicians) == 0:
            print("No technicians found.")
        else:
            utils.print_divider(options=options)
            print_options = options.copy()
            print_options.text_color = Term.RESET_BOLD_UNDERLINE
            utils.print_text_block(text="Current Technicians", top_border=False, bottom_border=False, options=print_options)

            technician_dict = {}
            for technician in technicians:
                key = f"Technician {technician['technician_id']}"
                technician_dict[key] = f"{technician['first_name']} {technician['last_name']}"

            utils.print_json_in_table_format(technician_dict, options=options)
            utils.print_blank_line(options=options)
            utils.print_divider(options=options)
    else:
        print(f"{response.json()}; Error code: {response.status_code}")

def display_technician_avg_ticket_times(print_options):
    options = print_options
    url = f"{api_url_base}Technicians/AvgTicketTimes"
    params = {}
    data = {}
    response = requests.get(url, params=params, data=data)
    if response.status_code == 200:
        technicians = response.json()
        if len(technicians) == 0:
            print("No technician times found.")
        else:
            utils.print_divider(options=options)

            utils.print_text_block(text="Average Ticket Times", top_border=False, bottom_border=False, options=options)

            technician_dict = {}
            key = "Technician Name"
            technician_dict[key] = "Average Ticket Time"
            for technician in technicians:
                key = f"{technician['first_name']} {technician['last_name']}"
                technician_dict[key] = f"{technician['average_ticket_time']}"

            utils.print_json_in_table_format(technician_dict, options=options)
            utils.print_blank_line(options=options)
            utils.print_divider(options=options)
    else:
        print(f"{response.json()}; Error code: {response.status_code}")

def display_technician_managers(print_options):
    options = print_options
    url = f"{api_url_base}Technicians/Manager"

    while True:
        utils.print_text_block(text="Please enter the id of the technician whose manager you would like to know.", bottom_border = False, options=options)
        utils.print_divider(options=options)
        user_input = utils.get_input("Enter a command: ")
        try:
            technician_id = int(user_input)
            break
        except:
            print("Invalid input. Please try again.")

    params = {"technician_id": f"{technician_id}"}
    data = {}
    response = requests.get(url, params=params, data=data)


    if response.status_code == 200:
        technician = response.json()

        utils.print_divider(options=options)

        utils.print_text_block(text="Technician Managers", top_border=False, bottom_border=False, options=options)

        technician_dict = {}
        key = "Technician"
        technician_dict[key] = "Manager"
        key = f"{technician['technician_first_name']} {technician['technician_last_name']}"
        manager = technician['manager']
        manager_name = f"{manager['first_name']} {manager['last_name']}"
        technician_dict[key] = manager_name

        utils.print_json_in_table_format(technician_dict, options=options)
        utils.print_blank_line(options=options)
        utils.print_divider(options=options)
    else:
        print(f"{response.json()}; Error code: {response.status_code}")

def display_ticket_information(print_options):
    options = print_options
    url = f"{api_url_base}Technicians/TicketsInfo"

    while True:
        utils.print_text_block(text="Please enter the id of the technician whose tickets you would like to view, or type 'cancel' to cancel.", bottom_border = False, options=options)
        utils.print_divider(options=options)
        user_input = utils.get_input("Enter a command: ")
        try:
            technician_id = int(user_input)
            break
        except:
            if user_input.lower() == "cancel":
                return
            print("Invalid input. Please try again.")

    params = {"technician_id": f"{technician_id}"}
    data = {}
    tickets_response = requests.get(url, params=params, data=data)

    url = f"{api_url_base}Technicians/Manager"
    params = {"technician_id": f"{technician_id}"}
    data = {}

    technician_response = requests.get(url, params=params, data=data)

    technician_name = ""

    if technician_response.status_code == 200:
        technician = technician_response.json()

        technician = technician_response.json()

        technician_name = f"{technician['technician_first_name']} {technician['technician_last_name']}".strip()
        if technician_name.lower().endswith('s'):
            technician_name += "' "
        else:
            technician_name += "'s "



    if tickets_response.status_code == 200:
        tickets = tickets_response.json()
        if len(tickets) == 0:
            utils.print_text_block(text=f"No tickets found for '{technician_name.strip()}'.", top_border=False, bottom_border=False, options=options)
        else:
            utils.print_divider(options=options)

            utils.print_text_block(text=f"{technician_name}Tickets", top_border=False, bottom_border=False, options=options)

            # Sort tickets in descending order based on open_date_time
            tickets.sort(key=lambda x: datetime.strptime(x['open_date_time'], '%a, %d %b %Y %H:%M:%S %Z'), reverse=True)

            for ticket in tickets:
                ticket_dict = {key: textwrap.fill(value, 50) if isinstance(value, str) and len(value) > 50 else value for key, value in ticket.items()}
                utils.print_json_in_table_format(ticket_dict, options=options)
                utils.print_blank_line(options=options)
                utils.print_divider(options=options)
                            
                # Add user prompt
                user_input = utils.get_input("Press enter to continue or type 'cancel' to stop: ")
                if user_input.lower() == 'cancel':
                    break

def run(base_url):
    global api_url_base
    api_url_base = base_url

    print_options = PrintOptions(border_marker_color=Term.GREEN, line_divider_color=Term.GREEN)
    utils.print_text_block(text="Technician Viewer", bottom_border = False, options=print_options)

    menu_options = ["1. Technician Names", "2. Technician Information"
        , "3. Average Ticket Times", "4. Technician\'s Manager", "5. Ticket Information", "0. Quit"]
    quit = False
    while not quit:
        print_options.alignment = 'center'
        utils.print_text_block(header="Options:", text=menu_options, options=print_options)
        user_input = utils.get_input("Enter a command: ")
        # user_input = input("Enter a command: ")

        if user_input == "1":
            display_technician_names(print_options)
        elif user_input == "2":
            display_technician_information(print_options)
        elif user_input == "3":
            display_technician_avg_ticket_times(print_options)
        elif user_input == "4":
            display_technician_managers(print_options)
        elif user_input == "5":
            display_ticket_information(print_options)
        elif user_input == "0":
            print("Exiting Technician Viewer.")
            quit = True
        else:
            print("Invalid command. Please try again.")
