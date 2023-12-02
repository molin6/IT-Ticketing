import requests
import json
import textwrap
from datetime import datetime
from utils import text_print_utils as utils
from utils.text_print_options import PrintOptions, Term


def display_user_information(print_options):
    options = print_options
    start = 0
    limit = None

    while True:

        utils.print_text_block(text="How many users would you like to view at a time? Please enter a whole number, or type 'all' to view all users.", bottom_border = False, options=options)
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


    url = f"{api_url_base}Users"

    get_more = True
    while get_more:
        params = {'start': start, 'limit': limit}
        data = {}
        response = requests.get(url, params=params, data=data)

        if response.status_code == 200:
            users = response.json()
            if len(users) == 0:
                print("No users found.")
                break
            utils.print_divider(options=options)

            for user in users:

                options.alignment = 'center'
                utils.print_text(f"Displaying User: {user['First Name']} {user['Last Name']}", options)

                options.line_divider_char = '-'
                utils.print_divider(options=options)

                utils.print_blank_line(options=options)

                ordered_keys = ['First Name', 'Last Name', 'Title', 'Email Address', 'Phone Number', 'Organization ID']
                rename_keys = {'Phone Number': 'Phone #', 'Organization ID': 'Organization Id'}

                utils.print_json_in_table_format(user, ordered_keys, rename_keys, options=options)

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
            utils.print_text_block(text="Would you like to view more users? Please enter 'yes' or 'no'.", bottom_border = False, options=options)
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


def run(base_url):
    global api_url_base
    api_url_base = base_url

    print_options = PrintOptions(border_marker_color=Term.MAGENTA, line_divider_color=Term.MAGENTA)
    utils.print_text_block("User Viewer", bottom_border = False, options=print_options)
        
    menu_options = ["1. User Information", "0. Main Menu"]
    quit = False
    while not quit:
        print_options.alignment = 'center'
        utils.print_text_block("Menu Options:", menu_options, options=print_options)
        user_input = utils.get_input("Enter a command: ")

        if user_input == "1":
            display_user_information(print_options)
        # elif user_input == "2":
        #     pass
        # elif user_input == "3":
        #     pass
        # elif user_input == "4":
        #     pass
        elif user_input == "0":
            print("Exiting User Viewer.")
            quit = True
        else:
            print("Invalid command. Please try again.")