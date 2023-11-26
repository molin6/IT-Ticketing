import requests
import json
from utils import text_print_utils as utils
from utils.text_print_options import PrintOptions, Term
from views import technician_view, ticket_view

api_url_base = "http://localhost:5000/"

index = 0

menu_options = ["1. Ticket Management","2. Technician Management", "0. Quit"]

def run_ticket_system():
    utils.print_text_block("Group 1 API Project - Ticket Viewer")
    utils.print_text_block("Main Menu", top_border = False, bottom_border = False)

    while True:
        utils.print_text_block("Menu Options:", menu_options)
        user_input = input("Enter a command: ")

        if user_input == "1":
            ticket_view.run(api_url_base)
        elif user_input == "2":
            technician_view.run(api_url_base)

        elif user_input == "0":
            print("Exiting the system.")
            break
        else:
            print("Invalid command. Please try again.")

        utils.print_text_block("Main Menu", top_border=True, bottom_border=False)

run_ticket_system()