import sqlite3
import importlib
import subprocess
import sys

def install_package(package_name: str):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def install_required_packages():
    """
    Install the required Python packages for the API project.

    This function installs the following packages:
    - sqlalchemy_utils
    - Faker
    - fastapi[all]

    If a package is already installed, it is skipped.

    Raises:
        Any exceptions raised by the `install_package()` function during the package installation.

    """
    packages = ['sqlalchemy_utils', 'Faker', 'fastapi[all]', 'Flask'] # 'flask'

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


