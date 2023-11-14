from tabulate import tabulate

def print_text(args = "", alignment='center', tab_spaces=0, screen_width=100, border_marker_char="|", line_divider_char="*", item_divider_char="|"):
    # Validate alignment input
    if alignment not in ['center', 'left', 'right']:
        raise ValueError("alignment must be 'center', 'left', or 'right'")

    if not isinstance(args, list) and not isinstance(args, str):
        raise TypeError("text must be a string or a list of strings")

    def align_text(text, available_width, alignment):
        # Add the specified number of spaces to the front of the text
        text = ' ' * (tab_spaces * 4) + text

        if alignment == 'center':
            return text.center(available_width)
        elif alignment == 'left':
            return text.ljust(available_width)
        elif alignment == 'right':
            return text.rjust(available_width)

    if isinstance(args, str):
        aligned_text = align_text(args, screen_width - 2, alignment)
        bounded_text = border_marker_char + aligned_text + border_marker_char
        print(bounded_text)
        return

    if isinstance(args, list):
        available_width = screen_width - 2
        # Start with an empty line
        current_line = ""
        for i, item in enumerate(args):
            # Add divider if not the first item in the line
            if current_line:
                item_with_divider = " " + item_divider_char + " " + item
            else:
                item_with_divider = item

            # Check if the item fits in the current line
            if len(current_line) + len(item_with_divider) <= available_width:
                current_line += item_with_divider
            else:
                aligned_text = align_text(current_line, available_width, alignment)
                bounded_text = border_marker_char + aligned_text + border_marker_char
                print(bounded_text)
               
                # Start a new line with the current item
                current_line = item

        # Print any remaining text in the current line
        if current_line:
            aligned_text = align_text(current_line, available_width, alignment)
            bounded_text = border_marker_char + aligned_text + border_marker_char
            print(bounded_text)

def print_divider(screen_width=100, line_divider_char="*", item_divider_char="|"):
    print_text(line_divider_char * (screen_width - 2), screen_width=screen_width, line_divider_char=line_divider_char, item_divider_char=item_divider_char)

def print_blank_line(screen_width=100, border_marker_char="|", item_divider_char="|"):
    print_text(screen_width=screen_width, border_marker_char=border_marker_char, item_divider_char=item_divider_char)

def print_text_block(header = "", text = "", footer = "", top_border = True, bottom_border = True, screen_width=100, border_marker_char="|", line_divider_char="*", item_divider_char="|"):
    if top_border:
        print_divider(screen_width=screen_width, line_divider_char=line_divider_char, item_divider_char=item_divider_char)

    print_blank_line(screen_width=screen_width, border_marker_char=border_marker_char, item_divider_char=item_divider_char)

    if header:
        print_text(header, screen_width=screen_width, border_marker_char=border_marker_char, item_divider_char=item_divider_char)

    if text:
        print_text(text, screen_width=screen_width, border_marker_char=border_marker_char, item_divider_char=item_divider_char)

    print_blank_line(screen_width=screen_width, border_marker_char=border_marker_char, item_divider_char=item_divider_char)

    if footer:
        print_text(footer, screen_width=screen_width, border_marker_char=border_marker_char, item_divider_char=item_divider_char)

    if bottom_border:
        print_divider(screen_width=screen_width, line_divider_char=line_divider_char, item_divider_char=item_divider_char)

def print_json_in_table_format(json_object, ordered_keys=None, rename_keys=None, tablefmt='fancy_grid', screen_width=100, border_marker_char="|"):
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
        print_text(line, screen_width=screen_width, border_marker_char=border_marker_char, alignment='left')
    
    
    # print(bordered_table_string)

def add_border_to_string(s, border_marker_char='|', padding=2):
    lines = s.split('\n')
    for line in lines:
        print_text(line, screen_width=screen_width, border_marker_char=border_marker_char)


    # lines = [f"{border_marker_char}{line.center(width)}{border_marker_char}" for line in lines]
    return f"{border_line}\n" + "\n".join(lines) + f"\n{border_line}"
