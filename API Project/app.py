from controllers import main_controller


global install_dependencies
global start_server
global reset_database

install_dependencies = False
start_server = False
reset_database = False

main_controller.load_data_and_start_api(install_dependencies, start_server, reset_database)






# print(read_technician_names())
# print(read_technician_avg_ticket_times())
# print(read_user_ticket_counts())
# print(read_user_ticket_counts(1))
# print(read_department_avg_resolution_time())
# print(read_technician_ticketinfo())
# print(read_organizations_tickets_count())




