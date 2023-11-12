import utils
api_url_base = "http://localhost:5000"

quit = False
index = 0

menu_options = ["1. View all tickets", "2. View a ticket", "0. Quit"]

def run_ticket_system():
    utils.print_divider()
    utils.print_main_header()
    utils.print_view_header("Main Menu")
    global quit
    global index
    while not quit:
        utils.print_blank_line()
        utils.print_text("Menu Options:")
        utils.print_text(menu_options)
        utils.print_blank_line()
        utils.print_divider()
        user_input = input("Enter a command: ")
        if user_input == "1":
            print("You selected Option 1.")
            # Add code to handle Option 1 here.
        elif user_input == "2":
            print("You selected Option 2.")
            # Add code to handle Option 2 here.
        elif user_input == "3":
            print("Exiting the system.")
            quit = True
        else:
            print("Invalid command. Please try again.")



run_ticket_system()





