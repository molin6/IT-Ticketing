from controllers import api_controller
from database_initialization import setup_db

def load_data_and_start_api(install_dependencies, start_server, reset_database, populate_database):

    # Create the database
    # base_model.create_engine_and_database()

    if reset_database:
        setup_db.drop_all_tables()

    setup_db.create_engine_and_database()


    # Populate the database tables
    if populate_database:
        setup_db.populate_database_tables()
        setup_db.reset_organization_names()
        setup_db.reset_department_names()    

    # Start API Server
    if start_server:
        api_controller.run()
