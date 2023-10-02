import sqlite3
import importlib
import subprocess
import sys

def drop_all_tables(db_file_name : str = 'it_ticketing_system.db'):
    cnn = sqlite3.connect(db_file_name)
    cur = cnn.cursor()
    table_names = []
    results = cur.execute("SELECT tbl_name FROM sqlite_master")
    for table_name in results:
        table_names.append(table_name[0])

    for table_name in table_names:
        cur.execute(f'DROP TABLE IF EXISTS {table_name}')
        print(f'Dropped table \'{table_name}\'')

    cnn.close()

def install_package(package_name: str):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def install_required_packages():
    packages = ['sqlalchemy_utils', 'Faker', 'fastapi[all]']

    for package in packages:
        try:
            importlib.import_module(package)
            print(f"{package} is already installed.")
        except ModuleNotFoundError:
            print(f"{package} not found. Installing...")
            install_package(package)
            print(f"{package} has been installed.")

def bool_to_yes_no(value) -> str:
    if value == 0:
        return 'NO'
    elif value == 1:
        return 'YES'

def print_database_definitions(db_file_name : str = 'it_ticketing_system.db'):
    cnn = sqlite3.connect(db_file_name)
    cur = cnn.cursor()
    tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

    for table in tables:
        print('------------------')
        print('Table Name: ' + table[0])
        print('------------------')
        columns = cur.execute(f'PRAGMA table_info(\'%s\');' % table[0]).fetchall()
        for column in columns:
            col_id, col_name, col_type, col_notnull, col_default, col_pk = column
            print(f"  Column: {col_name}")
            print(f"    Type: {col_type}")
            print(f"    Not Null: {bool_to_yes_no(col_notnull)}")
            print(f"    Default Value: {col_default}")
            print(f"    Primary Key: {bool_to_yes_no(col_pk)}")

    cnn.close()
