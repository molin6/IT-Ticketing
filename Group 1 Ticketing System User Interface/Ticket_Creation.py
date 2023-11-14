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

if __name__ == "__main__":
    create_ticket()
