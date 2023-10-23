from utils import G1_common_tools

start_server = True
reset_database = False
populate_database = False

install_dependencies = False
if install_dependencies:
    # Install dependencies
    G1_common_tools.install_required_packages()


from controllers import main_controller
main_controller.load_data_and_start_api(install_dependencies, start_server, reset_database, populate_database)
