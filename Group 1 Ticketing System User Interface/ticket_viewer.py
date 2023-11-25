from utils import TextPrintUtils as utils
from views import technician_view
from funct import Ticket_ViewCreateDelteUpdate, create_ticket, delete_ticket, modify_ticket, view_ticket

api_url_base = "http://localhost:5000/"

index = 0

menu_options = ["1. Users","2. Technicians", "0. Quit"]

def run_ticket_system():
    utils.print_text_block("Group 1 API Project - Ticket Viewer")
    utils.print_text_block("Main Menu", top_border = False, bottom_border = False)

    quit = False
    while not quit:
        utils.print_text_block("Menu Options:", menu_options)
        user_input = input("Enter a command: ")

        if user_input == "1":
            print("\nTicket Management System")
            print("1. Create a Ticket")
            print("2. Delete a Ticket")
            print("3. Modify a Ticket")
            print("4. View a Ticket")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                create_ticket()

            elif choice == "2":
                ticket_id = input("Enter the Ticket ID to delete: ")
                result = delete_ticket(ticket_id)
                print(result)

            elif choice == "3":
                ticket_id = input("Enter the Ticket ID to modify: ")
                ticket_data = {
                    "user_id": int(input("Enter User ID: ")),
                    "department_id": int(input("Enter Department ID: ")),
                    # Add other fields as needed
                }
                result = modify_ticket(ticket_id, ticket_data)
                print(result)

            elif choice == "4":
                ticket_id = input("Enter the Ticket ID to view: ")
                ticket_info = view_ticket(ticket_id)
                print(json.dumps(ticket_info, indent=2))

            elif choice == "5":
                print("Exiting the Ticket Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        elif user_input == "2":
            technician_view.run(api_url_base)
        elif user_input == "0":
            print("Exiting the system.")
            quit = True
        else:
            print("Invalid command. Please try again.")

        options = TextPrintOptions(top_border=True, bottom_border=False)
        utils.print_text_block("Main Menu", options)

run_ticket_system()