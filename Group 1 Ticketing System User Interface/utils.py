import textwrap
screen_width = 100
boundary_marker = "|"
divider_char = "*"

# def print_menu_options(options):
#     blank_line()
#     options_text = " | ".join(options)
#     centered_text = options_text.center(screen_width - 4)  # Subtract 4 for the boundary markers and padding
#     wrapped_lines = textwrap.wrap(centered_text, width=screen_width - 4, break_long_words=False, replace_whitespace=False)
#     for line in wrapped_lines:
#         padded_line = line.ljust(screen_width - 2)  # Add padding to the right
#         bounded_line = '*' + padded_line + '*'
#         print(bounded_line)
#     blank_line()
#     divider()
#     blank_line()





def centered_text(text):
    aligned_text = text.center(screen_width - 2)
    bounded_text = boundary_marker + aligned_text + boundary_marker
    print(bounded_text)

def left_aligned_text(text):
    aligned_text = text.ljust(screen_width - 2)
    bounded_text = boundary_marker + aligned_text + boundary_marker
    print(bounded_text)

def right_aligned_text(text):
    aligned_text = text.rjust(screen_width - 2)
    bounded_text = boundary_marker + aligned_text + boundary_marker
    print(bounded_text)

def divider():
    print(boundary_marker + divider_char * (screen_width - 2) + boundary_marker)

def blank_line():
    print(boundary_marker + " " * (screen_width - 2) + boundary_marker)

def print_main_header():
    blank_line()
    centered_text("Group 1 API Project - Ticket Viewer")
    blank_line()
    divider()
    blank_line()

def print_footer():
    blank_line()
    divider()
    blank_line()
    centered_text("End of Ticket Viewer")
    blank_line()

def print_view_header(text):
    blank_line()
    centered_text(text)
    blank_line()
    divider()
    blank_line()

def print_error(error):
    blank_line()
    left_aligned_text("Error: " + error)
    blank_line()
    divider()
    blank_line()
