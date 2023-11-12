import textwrap

screen_width = 100
boundary_marker = "|"
divider_char = "*"

def print_text(args, alignment='center'):
    # Validate alignment input
    if alignment not in ['center', 'left', 'right']:
        raise ValueError("alignment must be 'center', 'left', or 'right'")

    if not isinstance(args, list) and not isinstance(args, str):
        raise TypeError("text must be a string or a list of strings")

    def align_text(text, available_width, alignment):
        if alignment == 'center':
            return text.center(available_width)
        elif alignment == 'left':
            return text.ljust(available_width)
        elif alignment == 'right':
            return text.rjust(available_width)

    if isinstance(args, str):
        aligned_text = align_text(args, screen_width - 2, alignment)
        bounded_text = boundary_marker + aligned_text + boundary_marker
        print(bounded_text)
        return

    if isinstance(args, list):
        available_width = screen_width - 2
        # Start with an empty line
        current_line = ""
        for i, item in enumerate(args):
            # Add divider if not the first item in the line
            if current_line:
                item_with_divider = " " + boundary_marker + " " + item
            else:
                item_with_divider = item

            # Check if the item fits in the current line
            if len(current_line) + len(item_with_divider) <= available_width:
                current_line += item_with_divider
            else:
                aligned_text = align_text(current_line, available_width, alignment)
                bounded_text = boundary_marker + aligned_text + boundary_marker
                print(bounded_text)
               
                # Start a new line with the current item
                current_line = item

        # Print any remaining text in the current line
        if current_line:
            aligned_text = align_text(current_line, available_width, alignment)
            bounded_text = boundary_marker + aligned_text + boundary_marker
            print(bounded_text)

def print_divider():
    print(boundary_marker + divider_char * (screen_width - 2) + boundary_marker)

def print_blank_line():
    print(boundary_marker + " " * (screen_width - 2) + boundary_marker)

def print_main_header():
    print_blank_line()
    print_text("Group 1 API Project - Ticket Viewer")
    print_blank_line()
    print_divider()

def print_footer():
    print_blank_line()
    print_divider()
    print_blank_line()
    print_text("End of Ticket Viewer")
    print_blank_line()

def print_view_header(text):
    print_blank_line()
    print_text(text)
    print_blank_line()
    print_divider()

def print_error(error):
    print_blank_line()
    print_text("Error: " + error, 'left')
    print_blank_line()
    print_divider()
    print_blank_line()
