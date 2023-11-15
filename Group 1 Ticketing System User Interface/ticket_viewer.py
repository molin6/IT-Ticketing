from utils import TextPrintUtils as utils
from views import technician_view

api_url_base = "http://localhost:5000/"

index = 0

menu_options = ["1. Technicians", "0. Quit"]

def run_ticket_system():
    utils.print_text_block("Group 1 API Project - Ticket Viewer")
    utils.print_text_block("Main Menu", top_border = False, bottom_border = False)

    quit = False
    while not quit:
        utils.print_text_block("Menu Options:", menu_options)
        user_input = input("Enter a command: ")

        if user_input == "1":
            technician_view.run(api_url_base)
        elif user_input == "0":
            print("Exiting the system.")
            quit = True
        else:
            print("Invalid command. Please try again.")

        options = TextPrintOptions(top_border=True, bottom_border=False)
        utils.print_text_block("Main Menu", options)

run_ticket_system()