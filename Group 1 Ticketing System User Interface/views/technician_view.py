from utils import TextPrintUtils as utils
import requests
from utils.TextPrintOptions import PrintOptions
from utils.TextPrintOptions import Term

def display_technicians():
    url = f"{api_url_base}Technicians"
    params = {}
    data = {}
    response = requests.get(url, params=params, data=data)

    if response.status_code == 200:
        technicians = response.json()
        options = PrintOptions(border_marker_color=Term.GREEN, line_divider_color=Term.GREEN)
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

    print()

def run(base_url):
    global api_url_base
    api_url_base = base_url
    utils.print_text_block("Technician Viewer", bottom_border = False)

    menu_options = ["1. Display Technicians", "0. Quit"]
    quit = False
    while not quit:
        utils.print_text_block("Menu Options:", menu_options)
        user_input = input("Enter a command: ")

        if user_input == "1":
            display_technicians()
        elif user_input == "0":
            print("You selected Option 0 in the Technician Viewer.")
            print("Exiting Technician Viewer.")
            quit = True
        else:
            print("Invalid command. Please try again.")
