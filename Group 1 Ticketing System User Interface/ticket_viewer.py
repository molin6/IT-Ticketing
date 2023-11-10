import utils
api_url_base = "http://localhost:5000"

quit = False
index = 0

menu_options = ["1. View all tickets", "2. View a ticket", "3. Quit", "1. View all tickets", "2. View a ticket", "3. Quit"
                , "1. View all tickets", "2. View a ticket", "3. Quit", "1. View all tickets", "2. View a ticket", "3. Quit"]


def print_menu_options(options):
    utils.blank_line()

    remaining_width = utils.screen_width - 2  # Subtract 2 for the boundary markers
    option_lines = []
    option_line = ""
    for option in options:
        option_length = len(option)

        #TODO: pick up here tomorrow, I'm needing to finish the functionality to print the menu options in the center of the screen
        # with each line centered and wrapped to the next line if it's too long to fit on the current line, with
        # the boundary markers and padding included in the calculation of the width of the screen.

        if option_length > remaining_width:
            # The option is too long to fit on the current line, so print it on the next line
            utils.left_aligned_text(option)
            remaining_width = utils.screen_width - 2  # Subtract 2 for the boundary markers
        else:
            # The option fits on the current line, so print it there
            remaining_width -= option_length + 3  # Add 3 for the boundary markers and padding
        
        utils.left_aligned_text(option)


    # options_text = " | ".join(options)
    # centered_text = options_text.center(utils.screen_width - 4)  # Subtract 4 for the boundary markers and padding
    # wrapped_lines = utils.textwrap.wrap(centered_text, width=utils.screen_width - 4, break_long_words=False, replace_whitespace=False)
    # for line in wrapped_lines:
    #     padded_line = line.ljust(utils.screen_width - 2)  # Add padding to the right
    #     bounded_line = utils.boundary_marker + padded_line + utils.boundary_marker
    #     print(bounded_line)
    utils.blank_line()
    utils.divider()
    utils.blank_line()

def run_ticket_system():
    utils.divider()
    utils.print_main_header()
    utils.print_view_header("Main Menu")
    global quit
    global index
    while not quit:
        print_menu_options(menu_options)
        user_input = input("Enter a command: ")
        if user_input == "1":
            print("You selected Option 1.")
            # Add code to handle Option 1 here.
        elif user_input == "2":
            print("You selected Option 2.")
            # Add code to handle Option 2 here.
        elif user_input == "3":
            print("Exiting the system.")
            quit = True
        else:
            print("Invalid command. Please try again.")
        index += 1
        if index >= 5:
            quit = True
    pass


run_ticket_system()








# def run_ticket_system():
#     global index
#     global quit
#     while not quit:
#         print("1. Option 1")
#         print("2. Option 2")
#         print("3. Quit")
#         user_input = input("Enter a command: ")
#         if user_input == "1":
#             print("You selected Option 1.")
#             # Add code to handle Option 1 here.
#         elif user_input == "2":
#             print("You selected Option 2.")
#             # Add code to handle Option 2 here.
#         elif user_input == "3":
#             print("Exiting the system.")
#             quit = True
#         else:
#             print("Invalid command. Please try again.")
#         index += 1
#         if index >= 5:
#             quit = True



