import requests
import json
from utils import text_print_utils as utils
from utils.text_print_options import PrintOptions, Term










def run(base_url):
    global api_url_base
    api_url_base = base_url

    print_options = PrintOptions(border_marker_color=Term.MAGENTA, line_divider_color=Term.MAGENTA, text_color=Term.MAGENTA)
    utils.print_text_block("User Viewer", bottom_border = False, options=print_options)

    menu_options = ["0. Quit"]
    quit = False
    while not quit:
        print_options.alignment = 'center'
        utils.print_text_block("Menu Options:", menu_options, options=print_options)
        user_input = input("Enter a command: ")

        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "0":
            print("Exiting User Viewer.")
            quit = True
        else:
            print("Invalid command. Please try again.")