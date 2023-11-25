import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:5000"  # Replace with the actual base URL of your API

def create_ticket():
    userid = int(input("Enter the ID of the user who created the ticket: "))
    departmetnid = int(input("Enter the ID of the department: "))
    priorticketid = int(input("Enter the ID of the prior ticket: "))
    ticketcategory = input("Enter the category of the ticket: ")
    subject = input("Enter the subject of the ticket: ")
    description = input("Enter the description of the ticket: ")

    # Automatically add the current date and time for the created_at field
    open_date_time = datetime.now().isoformat()
    close_date_time = 0
    status = "Open"

    ticket_data = {
        "user_id": userid,
        "department_id": departmetnid,
        "prior_ticket_id": priorticketid,
        "ticket_category": ticketcategory,
        "open_date_time": open_date_time,
        "close_date_time": close_date_time,
        "status": status,
        "description": description,
        "subject": subject
    }

    response = requests.post(f"{BASE_URL}/Tickets", json=ticket_data)

    if response.status_code == 200:
        print("Ticket created successfully.")
        print("Created Ticket Details:")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Failed to create ticket. Status code: {response.status_code}")
        print(response.text)

def delete_ticket(ticket_id):
    url = f"{BASE_URL}/Tickets?ticket_id={ticket_id}"
    response = requests.delete(url)
    return response.text

def modify_ticket(ticket_id, ticket_data):
    url = f"{BASE_URL}/Tickets?ticket_id={ticket_id}"
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, data=json.dumps(ticket_data), headers=headers)
    return response.text

def view_ticket(ticket_id):
    url = f"{BASE_URL}/Tickets?ticket_id={ticket_id}"
    response = requests.get(url)
    return response.json()

# def main():
#     while True:
#         print("\nTicket Management System")
#         print("1. Create a Ticket")
#         print("2. Delete a Ticket")
#         print("3. Modify a Ticket")
#         print("4. View a Ticket")
#         print("5. Exit")

#         choice = input("Enter your choice (1-5): ")

#         if choice == "1":
#             create_ticket()

#         elif choice == "2":
#             ticket_id = input("Enter the Ticket ID to delete: ")
#             result = delete_ticket(ticket_id)
#             print(result)

#         elif choice == "3":
#             ticket_id = input("Enter the Ticket ID to modify: ")
#             ticket_data = {
#                 "user_id": int(input("Enter User ID: ")),
#                 "department_id": int(input("Enter Department ID: ")),
#                 # Add other fields as needed
#             }
#             result = modify_ticket(ticket_id, ticket_data)
#             print(result)

#         elif choice == "4":
#             ticket_id = input("Enter the Ticket ID to view: ")
#             ticket_info = view_ticket(ticket_id)
#             print(json.dumps(ticket_info, indent=2))

#         elif choice == "5":
#             print("Exiting the Ticket Management System. Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please enter a number between 1 and 5.")

# if __name__ == "__main__":
#     main()
