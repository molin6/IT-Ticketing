import unittest
import sys
import os
from flask import Flask
import json

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
controller_directory = os.path.join(parent_dir, "API Project", "controllers")
sys.path.append(controller_directory)
model_directory = os.path.join(parent_dir, "API Project", "models")
sys.path.append(model_directory)
api_directory = os.path.join(parent_dir, "API Project")
sys.path.append(api_directory)

import api_controller # type: ignore            #THE PRECEDING COMMENT SUPPRESSES THE IMPORT ERROR
from api_controller import app # type: ignore   #THE PRECEDING COMMENT SUPPRESSES THE IMPORT ERROR

def run_test_case(test_case_func, *args, **kwargs):
    print("*" * 100)
    print(f"\nTesting {test_case_func.__name__}({', '.join(map(str, args))})...\n")
    print("*" * 100)
    response, status_code = test_case_func(*args, **kwargs)
    print("\nStatus Code: " + str(status_code))
    print("Response: " + str(response))
    print("JSON Data:")
    print(json.dumps(response.get_json(), indent=4))            
    print("\nTest complete.\n")
    print("*" * 100)

class TestApiController(unittest.TestCase):

    def select_technicians_without_limit(self):
        with app.app_context(), app.test_request_context():
            run_test_case(api_controller.select_technicians)
    
    def select_technicians_with_limit(self):
        limit = 1
        with app.app_context(), app.test_request_context(f'/?limit={limit}'):
            run_test_case(api_controller.select_technicians)

    def select_technicians_with_start_and_limit(self):
        start = 0
        limit = 4
        with app.app_context(), app.test_request_context(f'/?start={start}&limit={limit}'):
            run_test_case(api_controller.select_technicians)

    def read_technician_names(self):
        with app.app_context(), app.test_request_context():
            run_test_case(api_controller.read_technician_names)

    def read_technician_avg_ticket_times(self):
        with app.app_context(), app.test_request_context():
            run_test_case(api_controller.read_technician_avg_ticket_times)

    def read_technician_ticketinfo(self):
        technician_id = 1
        with app.app_context(), app.test_request_context(f'/?technician_id={technician_id}'):
            run_test_case(api_controller.read_technician_ticketinfo)

    def get_technicians_manager(self):
        technician_id = 1
        with app.app_context(), app.test_request_context(f'/?technician_id={technician_id}'):
            run_test_case(api_controller.get_technicians_manager)

    def update_technician_manager(self):
        technician_id = 2
        manager_user_id = 4
        with app.app_context(), app.test_request_context(f'/?technician_id={technician_id}&manager_user_id={manager_user_id}'):
            run_test_case(api_controller.update_technician_manager)

    def read_ticket_lines_with_start_and_limit(self):
        start = 2
        limit = 5
        with app.app_context(), app.test_request_context(f'/?start={start}&limit={limit}'):
            run_test_case(api_controller.read_ticket_lines)

    def read_ticket_lines_without_limit(self):
        with app.app_context(), app.test_request_context():
            run_test_case(api_controller.read_ticket_lines)

    def read_ticket_lines_with_limit(self):
        limit = 1
        with app.app_context(), app.test_request_context(f'/?limit={limit}'):
            run_test_case(api_controller.read_ticket_lines)

    def read_tickets_without_limit(self):
        with app.app_context(), app.test_request_context():
            run_test_case(api_controller.read_tickets)

    def read_tickets_with_limit(self):
        limit = 1
        with app.app_context(), app.test_request_context(f'/?limit={limit}'):
            run_test_case(api_controller.read_tickets)

    def read_tickets_with_start_and_limit(self):
        start = 2
        limit = 4
        with app.app_context(), app.test_request_context(f'/?start={start}&limit={limit}'):
            run_test_case(api_controller.read_tickets)

    def create_ticket(self):
        ticket_data = {
            "user_id": 1,
            "department_id": 2,
            "prior_ticket_id": None,
            "ticket_category": "Non-Emergency",
            "open_date_time": "2021-04-01 00:00:00 CST",
            "close_date_time": "2021-04-01 00:00:00 CST",
            "status": "Open",
            "description": "This is a test ticket.",
            "subject": "Test Ticket"
        }
        with app.app_context(), app.test_request_context(json=ticket_data):
            run_test_case(api_controller.create_ticket)

    def update_ticket(self):
        ticket_id = 381
        ticket_data = {
            "user_id": 1,
            "department_id": 2,
            "prior_ticket_id": None,
            "ticket_category": "Non-Emergency",
            "open_date_time": "2021-05-01 00:00:00 CST",
            "close_date_time": "2021-05-01 00:00:00 CST",
            "status": "Closed",
            "description": "This is a test update.",
            "subject": "Test Ticket Update"
        }
        with app.app_context(), app.test_request_context(f'/?ticket_id={ticket_id}', json=ticket_data):
            run_test_case(api_controller.update_ticket)

    def read_users_without_limit(self):
        with app.app_context(), app.test_request_context():
            run_test_case(api_controller.read_users)
    
    def read_users_with_limit(self):
        limit = 1
        with app.app_context(), app.test_request_context(f'/?limit={limit}'):
            run_test_case(api_controller.read_users)

    def read_users_with_start_and_limit(self):
        start = 1
        limit = 3
        with app.app_context(), app.test_request_context(f'/?start={start}&limit={limit}'):
            run_test_case(api_controller.read_users)

    def read_user_ticket_counts(self):
        user_id = 4
        with app.app_context(), app.test_request_context(f'/?user_id={user_id}'):
            run_test_case(api_controller.read_user_ticket_counts)

    def delete_user(self):
        user_id = 6
        with app.app_context(), app.test_request_context(f'/?user_id={user_id}'):
            run_test_case(api_controller.delete_user)

    def read_organizations_without_limit(self):
        with app.app_context(), app.test_request_context():
            run_test_case(api_controller.read_organizations)

    def read_organizations_with_limit(self):
        limit = 1
        with app.app_context(), app.test_request_context(f'/?limit={limit}'):
            run_test_case(api_controller.read_organizations)

    def read_organizations_with_start_and_limit(self):
        start = 2
        limit = 1
        with app.app_context(), app.test_request_context(f'/?start={start}&limit={limit}'):
            run_test_case(api_controller.read_organizations)

    def read_organizations_tickets_count(self):
        with app.app_context(), app.test_request_context():
            run_test_case(api_controller.read_organizations_tickets_count)

    def read_departments_without_limit(self):
        with app.app_context(), app.test_request_context():
            run_test_case(api_controller.read_departments)

    def read_departments_with_limit(self):
        limit = 1
        with app.app_context(), app.test_request_context(f'/?limit={limit}'):
            run_test_case(api_controller.read_departments)

    def read_departments_with_start_and_limit(self):
        start = 1
        limit = 2
        with app.app_context(), app.test_request_context(f'/?start={start}&limit={limit}'):
            run_test_case(api_controller.read_departments)

    def read_department_avg_resolution_time(self):
        department_id = 2
        with app.app_context(), app.test_request_context(f'/?department_id={department_id}'):
            run_test_case(api_controller.read_department_avg_resolution_time)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'
                        , 'TestApiController.select_technicians_without_limit'
                        , 'TestApiController.select_technicians_with_limit'
                        , 'TestApiController.select_technicians_with_start_and_limit'
                        , 'TestApiController.read_technician_names'
                        , 'TestApiController.read_technician_avg_ticket_times'
                        , 'TestApiController.read_technician_ticketinfo'
                        , 'TestApiController.get_technicians_manager'
                        # , 'TestApiController.update_technician_manager'
                        , 'TestApiController.read_ticket_lines_without_limit'
                        , 'TestApiController.read_ticket_lines_with_limit'
                        , 'TestApiController.read_ticket_lines_with_start_and_limit'
                        , 'TestApiController.read_tickets_without_limit'
                        , 'TestApiController.read_tickets_with_limit'
                        , 'TestApiController.read_tickets_with_start_and_limit'
                        # , 'TestApiController.create_ticket'
                        # , 'TestApiController.update_ticket'
                        , 'TestApiController.read_users_without_limit'
                        , 'TestApiController.read_users_with_limit'
                        , 'TestApiController.read_users_with_start_and_limit'
                        , 'TestApiController.read_user_ticket_counts'
                        # , 'TestApiController.delete_user'
                        , 'TestApiController.read_organizations_without_limit'
                        , 'TestApiController.read_organizations_with_limit'
                        , 'TestApiController.read_organizations_with_start_and_limit'
                        , 'TestApiController.read_organizations_tickets_count'
                        , 'TestApiController.read_departments_without_limit'
                        , 'TestApiController.read_departments_with_limit'
                        , 'TestApiController.read_departments_with_start_and_limit'
                        , 'TestApiController.read_department_avg_resolution_time'
                       ], exit=False)
