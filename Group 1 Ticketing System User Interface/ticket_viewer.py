import utils
from views import technician_view

api_url_base = "http://localhost:5000/"


index = 0

menu_options = ["1. Technicians", "0. Quit"]
# from tabulate import tabulate
def run_ticket_system():
    # table = [['Name', 'Age'], ['Alice', 25], ['Bob', 30]]

    # formats = ['plain', 'simple', 'grid', 'fancy_grid', 'pipe', 'orgtbl', 'jira', 'presto', 'pretty', 'psql', 'rst', 'mediawiki', 'moinmoin', 'youtrack', 'html', 'latex', 'latex_raw', 'latex_booktabs', 'textile']

    # for fmt in formats:
    #     print(f"Format: {fmt}")
    #     print(tabulate(table, headers='firstrow', tablefmt=fmt))
    #     print("\n")


    utils.print_text_block("Group 1 API Project - Ticket Viewer")
    utils.print_text_block("Main Menu", top_border = False, bottom_border = False)

    quit = False
    while not quit:
        utils.print_text_block("Menu Options:", menu_options)
        user_input = input("Enter a command: ")

        if user_input == "1":
            technician_view.run(api_url_base)
            utils.print_text_block("Main Menu", top_border = True, bottom_border = False)
        elif user_input == "0":
            print("Exiting the system.")
            quit = True
        else:
            print("Invalid command. Please try again.")



run_ticket_system()





