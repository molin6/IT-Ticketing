import utils
import requests

def display_technicians():
    url = f"{api_url_base}Technicians"
    response = requests.get(url)
    params = {}
    data = {}
    response = requests.get(url, params=params, data=data)
    if response.status_code == 200:
        technicians = response.json()
        for technician in technicians:




            utils.print_text(f"Displaying Technician: {technician['technician_user_data']['first_name']} {technician['technician_user_data']['last_name']}", alignment = 'left')

            ordered_keys = ['technician_id', 'first_name', 'last_name']
            rename_keys = {'technician_id': 'Technician Id', 'first_name': 'First Name', 'last_name': 'Last Name'}

            utils.print_json_in_table_format(technician['technician_user_data'], ordered_keys, rename_keys)

            # utils.print_text(f"Displaying Technician: {technician['technician_user_data']['first_name']} {technician['technician_user_data']['last_name']}", alignment = 'left')

            # utils.print_text(f"Technician Id: {technician['technician_id']}", tab_spaces = 1, alignment = 'left')
            # utils.print_text(f"User Id: {technician['technician_user_data']['user_id']}", tab_spaces = 1, alignment = 'left')
            # utils.print_text(f"First Name: {technician['technician_user_data']['first_name']}", tab_spaces = 1, alignment = 'left')
            # utils.print_text(f"Last Name: {technician['technician_user_data']['last_name']}", tab_spaces = 1, alignment = 'left')
            # utils.print_text(f"Title: {technician['technician_user_data']['title']}", tab_spaces = 1, alignment = 'left')
            # utils.print_text(f"Email Address: {technician['technician_user_data']['email_address']}", tab_spaces = 1, alignment = 'left')
            # utils.print_text(f"Phone Number: {technician['technician_user_data']['phone_number']}", tab_spaces = 1, alignment = 'left')
            # utils.print_text(f"Organization Id: {technician['technician_user_data']['organization_id']}", tab_spaces = 1, alignment = 'left')

            # utils.print_text(f"Manager's User Id: {technician['manager_user_id']}", tab_spaces = 2, alignment = 'left')
            utils.print_blank_line()



    else:
        print(f"{response.json()}; Error code: {response.status_code}")


def run(base_url):
    global api_url_base
    api_url_base = base_url
    utils.print_text_block("Technician Viewer", bottom_border = False)

    menu_options = ["1. Display Technicians", "0. Quit"]
    quit = False
    while not quit:
        utils.print_text_block("Menu Options:", menu_options)
        user_input = input("Enter a command: ")

        if user_input == "1":
            display_technicians()
        elif user_input == "0":
            print("You selected Option 0 in the Technician Viewer.")
            print("Exiting Technician Viewer.")
            quit = True
        else:
            print("Invalid command. Please try again.")





# def print_technician_names(technician_names):

#     max_length = max(len(name) for name in technician_names)
#     return_array = []

#     header_length = len('Technicians')
#     if header_length > max_length:
#         max_length = header_length
#     header_space = max_length - header_length
#     header_sides = header_space // 2
#     return_array.append(f'+ {"-" * max_length} +')
#     return_array.append(f'| {" " * header_sides}Technicians{" " * header_sides} |')
#     return_array.append(f'+ {"-" * max_length} +')
#     for name in technician_names:
#         return_array.append(f'| {name.ljust(max_length)} |')
#     return_array.append(f'+ {"-" * max_length} +')
#     return return_array
