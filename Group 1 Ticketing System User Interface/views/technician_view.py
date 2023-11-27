import requests
import json
from utils import text_print_utils as utils
from utils.text_print_options import PrintOptions, Term

def display_technician_information(print_options):
    options = print_options
    start = 0
    limit = None

    while True:
        utils.print_text_block("How many technicians would you like to view at a time? Please enter a whole number, or type 'all' to view all technicians.", bottom_border = False, options=options)
        utils.print_divider(options=options)
        user_input = input("Enter a command: ")
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
                options.text_color = Term.BLUE_BOLD
                utils.print_text(f"Displaying Technician: {technician['technician_user_data']['first_name']} {technician['technician_user_data']['last_name']}", options)

                options.line_divider_char = '-'
                utils.print_divider(options=options)

                utils.print_blank_line(options=options)

                ordered_keys = ['technician_id', 'technician_user_id', 'manager_user_id']
                rename_keys = {'technician_id': 'Technician Id', 'technician_user_id': 'Technician User Id', 'manager_user_id': 'Technician\'s Manager\'s Id'}

                options.tab_spaces = 0
                options.alignment = 'left'
                options.text_color = Term.GREEN
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
            utils.print_text_block("Would you like to view more technicians? Please enter 'yes' or 'no'.", bottom_border = False, options=options)
            utils.print_divider(options=options)
            user_input = input("Enter a command: ")
            if user_input == "yes":
                get_more = True
                break
            elif user_input == "no":
                get_more = False
                break
            else:
                print("Invalid input. Please try again.")
    options.text_color = Term.GREEN


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
            options.text_color = Term.BLUE_BOLD
            utils.print_divider(options=options)

            utils.print_text_block("Current Technicians", top_border=False, bottom_border=False, options=options)

            technician_dict = {}
            for technician in technicians:
                key = f"Technician {technician['technician_id']}"
                technician_dict[key] = f"{technician['first_name']} {technician['last_name']}"

            utils.print_json_in_table_format(technician_dict, options=options)
            utils.print_blank_line(options=options)
            utils.print_divider(options=options)
    else:
        print(f"{response.json()}; Error code: {response.status_code}")
    options.text_color = Term.GREEN

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
            options.text_color = Term.BLUE_BOLD
            utils.print_divider(options=options)

            utils.print_text_block("Average Ticket Times", top_border=False, bottom_border=False, options=options)

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

    options.text_color = Term.GREEN

def display_technician_managers(print_options):
    options = print_options
    url = f"{api_url_base}Technicians/Manager"

    while True:
        utils.print_text_block("Please enter the id of the technician whose manager you would like to know.", bottom_border = False, options=options)
        utils.print_divider(options=options)
        user_input = input("Enter a command: ")
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
        options.text_color = Term.BLUE_BOLD
        # options = PrintOptions(border_marker_color=Term.GREEN, line_divider_color=Term.GREEN, alignment='center', text_color=Term.BLUE_BOLD)
        utils.print_divider(options=options)

        utils.print_text_block("Technician Managers", top_border=False, bottom_border=False, options=options)

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

    options.text_color = Term.GREEN

def run(base_url):
    global api_url_base
    api_url_base = base_url

    print_options = PrintOptions(border_marker_color=Term.GREEN, line_divider_color=Term.GREEN, text_color=Term.GREEN)
    utils.print_text_block("Technician Viewer", bottom_border = False, options=print_options)

    menu_options = ["1. Display Technician Names", "2. Display Technician Information"
        , "3. Display Average Ticket Times", "4. Display Technician Manager", "0. Quit"]
    quit = False
    while not quit:
        print_options.alignment = 'center'
        utils.print_text_block("Menu Options:", menu_options, options=print_options)
        user_input = input("Enter a command: ")

        if user_input == "1":
            display_technician_names(print_options)
        elif user_input == "2":
            display_technician_information(print_options)
        elif user_input == "3":
            display_technician_avg_ticket_times(print_options)
        elif user_input == "4":
            display_technician_managers(print_options)
        elif user_input == "0":
            print("Exiting Technician Viewer.")
            quit = True
        else:
            print("Invalid command. Please try again.")
