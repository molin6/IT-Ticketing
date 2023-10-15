from controllers import main_controller


global install_dependencies
global start_server
global reset_database

install_dependencies = False
start_server = True
reset_database = False
populate_database = False

main_controller.load_data_and_start_api(install_dependencies, start_server, reset_database, populate_database)
