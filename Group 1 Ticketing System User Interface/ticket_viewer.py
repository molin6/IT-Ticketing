from utils import TextPrintUtils as utils
from views import technician_view
from funct import Ticket_ViewCreateDelteUpdate
import json

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
            print("4. View a Ticket/Tickets")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                Ticket_ViewCreateDelteUpdate.create_ticket()

            elif choice == "2":
                ticket_id = input("Enter the Ticket ID to delete: ")
                result = Ticket_ViewCreateDelteUpdate.delete_ticket(ticket_id)
                print(result)

            elif choice == "3":
                ticket_id = input("Enter the Ticket ID to view and modify: ")
                ticket_info = Ticket_ViewCreateDelteUpdate.view_ticket(ticket_id)
                print("Ticket Details:")
                print(json.dumps(ticket_info, indent=2))

                modify_choice = input("Do you want to modify this ticket? (yes/no): ").lower()
                if modify_choice == "yes":
                    ticket_data = {
                        "user_id": int(input("Enter User ID: ")),
                        "department_id": int(input("Enter Department ID: ")),
                        "prior_ticket_id": int(input("Enter Prior Ticket ID: ")),
                        "ticket_category": input("Enter Ticket Category: "),
                        "description": input("Enter Description: "),
                        "subject": input("Enter Subject: ")
                    }
                    result = Ticket_ViewCreateDelteUpdate.modify_ticket(ticket_id, ticket_data)
                    print(result)
                    if "Successfully updated the ticket" in result:
                        print("Ticket updated successfully!")
                    else:
                        print("Failed to update the ticket.")
                        break  # Exit the loop after modifying the ticket
                else:
                    print("Ticket not modified.")
                    break


            elif choice == "4":
                view_choice = input("Do you want to view one ticket or all tickets? (one/all): ").lower()

                if view_choice == "one":
                    ticket_id = input("Enter the Ticket ID to view: ")
                    ticket_info = Ticket_ViewCreateDelteUpdate.view_ticket(ticket_id)
                    print(json.dumps(ticket_info, indent=2))
                elif view_choice == "all":
                    Ticket_ViewCreateDelteUpdate.view_all_tickets()
                else:
                    print("Invalid choice. Please enter 'one' or 'all'.")
                    
            elif choice == "0":
                print("Exiting the Ticket Management System. Goodbye!")
                break

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