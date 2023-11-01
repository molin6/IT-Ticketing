from database_initialization import setup_db

setup_db.drop_all_tables()
setup_db.create_engine_and_database()
setup_db.populate_database_tables()
setup_db.reset_organization_names()
setup_db.reset_department_names()


