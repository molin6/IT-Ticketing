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

import api_controller
from api_controller import app

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
        limit = 1
        with app.app_context(), app.test_request_context():
            run_test_case(api_controller.select_technicians)
    
    def select_technicians_with_limit(self):
        limit = 1
        with app.app_context(), app.test_request_context(f'/?limit={limit}'):
            run_test_case(api_controller.select_technicians)

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
        technician_id = 1
        manager_user_id = 4
        with app.app_context(), app.test_request_context(f'/?technician_id={technician_id}&manager_user_id={manager_user_id}'):
            run_test_case(api_controller.update_technician_manager)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'
                        # , 'TestApiController.select_technicians_without_limit'
                        # , 'TestApiController.select_technicians_with_limit'
                        # , 'TestApiController.read_technician_avg_ticket_times'
                        # , 'TestApiController.read_technician_ticketinfo'
                        , 'TestApiController.get_technicians_manager'
                        # , 'TestApiController.update_technician_manager'
                        ], exit=False)