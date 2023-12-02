import os
import textwrap
from textwrap import wrap
from tabulate import tabulate
from .text_print_options import PrintOptions, Term

def print_text(args = "", options: PrintOptions = None):
    if options is None:
        options = PrintOptions()

    # Validate alignment input
    if options.alignment not in ['center', 'left', 'right']:
        raise ValueError("alignment must be 'center', 'left', or 'right'")

    if not isinstance(args, list) and not isinstance(args, str):
        raise TypeError("text must be a string or a list of strings")

    def align_text(text, available_width, alignment):
        # Add the specified number of spaces to the front of the text
        # text = ' ' * (options.tab_spaces * 4) + text

        # if alignment == 'center':
        #     return text.center(available_width)
        # elif alignment == 'left':
        #     return text.ljust(available_width)
        # elif alignment == 'right':
        #     return text.rjust(available_width)
        
        # Subtract the tab spaces from the available width
        available_width -= options.tab_spaces * 4

        if alignment == 'center':
            spaces_before = ' ' * ((available_width - len(text)) // 2)
            spaces_after = ' ' * (available_width - len(text) - len(spaces_before))
            return Term.RESET + ' ' * (options.tab_spaces * 4) + spaces_before + options.text_color + text.strip() + Term.RESET + spaces_after
        elif alignment == 'left':
            spaces_after = ' ' * (available_width - len(text))
            return Term.RESET + ' ' * (options.tab_spaces * 4) + options.text_color + text.lstrip() + Term.RESET + spaces_after
        elif alignment == 'right':
            spaces_before = ' ' * (available_width - len(text))
            return Term.RESET + ' ' * (options.tab_spaces * 4) + spaces_before + options.text_color + text.strip() + Term.RESET


    if isinstance(args, str):
        lines = textwrap.wrap(args, options.screen_width - 2)
        if len(lines) == 0:
            print(options.border_marker_color + options.border_marker_char + options.text_color + " " * (options.screen_width - 2) + options.border_marker_color + options.border_marker_char + options.text_color)
        else:
            for line in lines:
                aligned_text = align_text(line, options.screen_width - 2, options.alignment)
                print(options.border_marker_color + options.border_marker_char + options.text_color + aligned_text + options.border_marker_color + options.border_marker_char + options.text_color)
        return


    if isinstance(args, list):
        available_width = options.screen_width - 2
        # Start with an empty line
        current_line = ""
        for i, item in enumerate(args):
            # Add divider if not the first item in the line
            if current_line:
                item_with_divider = " " + options.item_divider_char + " " + item
            else:
                item_with_divider = item

            # Check if the item fits in the current line
            if len(current_line) + len(item_with_divider) <= available_width:
                current_line += item_with_divider
            else:
                aligned_text = align_text(current_line, available_width, options.alignment)
                print(options.border_marker_color + options.border_marker_char + options.text_color + aligned_text + options.border_marker_color + options.border_marker_char + options.text_color)
               
                # Start a new line with the current item
                current_line = item

        # Print any remaining text in the current line
        if current_line:
            aligned_text = align_text(current_line, available_width, options.alignment)
            print(options.border_marker_color + options.border_marker_char + options.text_color + aligned_text + options.border_marker_color + options.border_marker_char + options.text_color)

def print_divider(options: PrintOptions = None):
    if options is None:
        options = PrintOptions()
    
    text_print_options = options.copy()
    text_print_options.text_color = options.line_divider_color

    print_text(options.line_divider_char * (options.screen_width - 2), text_print_options)

def print_blank_line(options: PrintOptions = None):
    if options is None:
        options = PrintOptions()
    print_text(options=options)

def print_text_block(header = "", text = "", footer = "", top_border = True, bottom_border = True, options: PrintOptions = None):
    if options is None:
        options = PrintOptions()

    if top_border:
        print_divider(options)

    print_blank_line(options)

    if header:
        print_options = options.copy()
        print_options.text_color = Term.BOLD
        print_text(header, print_options)
        print_blank_line(options)

    if text:
        print_text(text, options)

    print_blank_line(options)

    if footer:
        print_text(footer, options)

    if bottom_border:
        print_divider(options)

def get_input(prompt, options: PrintOptions = None):
    if options is None:
        options = PrintOptions()
    
    text_print_options = options.copy()
    text_print_options.text_color = Term.YELLOW_BOLD

    return input(options.text_color + prompt + text_print_options.text_color)

def print_json_in_table_format(json_object, ordered_keys=None, rename_keys=None, tablefmt='fancy_grid', options: PrintOptions=None):
    if options is None:
        options = PrintOptions()

    table = []
    keys = ordered_keys if ordered_keys else json_object.keys()
    for key in keys:
        value = json_object.get(key)
        if rename_keys and key in rename_keys:
            key = rename_keys[key]
        if value is not None and isinstance(value, dict):
            for sub_key, sub_value in value.items():
                if rename_keys and sub_key in rename_keys:
                    sub_key = rename_keys[sub_key]
                table.append([sub_key, sub_value])
        else:
            table.append([key, value])
    table_string = tabulate(table, tablefmt=tablefmt)
    
    table_lines = table_string.split('\n')
    
    for line in table_lines:
        print_text(line, options)


# def print_json_in_table_format(json_object, ordered_keys=None, rename_keys=None, options: PrintOptions=None):
#     if options is None:
#         options = PrintOptions()

#     keys = ordered_keys if ordered_keys else json_object.keys()
#     if rename_keys:
#         keys = [rename_keys.get(key, key) for key in keys]
#     key_width = max(len(key) for key in keys) + 2
#     value_width = options.screen_width - key_width - 5

#     for key in keys:
#         value = json_object.get(key)
#         if rename_keys and key in rename_keys:
#             key = rename_keys[key]
#         if value is not None and isinstance(value, dict):
#             for sub_key, sub_value in value.items():
#                 if rename_keys and sub_key in rename_keys:
#                     sub_key = rename_keys[sub_key]
#                 print_table_row(sub_key, str(sub_value), key_width, value_width, options)
#         else:
#             print_table_row(key, str(value), key_width, value_width, options)
#     print_text('└' + '─' * (key_width - 1) + '┴' + '─' * (value_width - 3) + '┘', options)

# def print_table_row(key, value, key_width, value_width, options: PrintOptions=None):
#     if options is None:
#         options = PrintOptions()

#     print_text('├' + '─' * (key_width) + '┼' + '─' * (value_width - 2) + '┤', options)

#     # Wrap the value to the next line if it's too long
#     wrapper = textwrap.TextWrapper(width=value_width - 4)
#     lines = wrapper.wrap(value)

#     # Don't print the key value after the first line
#     print_text(f'│ {key.ljust(key_width - 4)} │ {lines[0].ljust(value_width - 4)} │', options)
#     for line in lines[1:]:
#         print_text(f'│ {" ".ljust(key_width - 4)} │ {line.ljust(value_width - 4)} │', options)

#     print_text('│ ' + ' ' * (key_width - 1) + '│ ' + ' ' * (value_width - 3) + '│', options)
