def print_technician_names(technician_names):

    max_length = max(len(name) for name in technician_names)
    return_array = []

    header_length = len('Technicians')
    if header_length > max_length:
        max_length = header_length
    header_space = max_length - header_length
    header_sides = header_space // 2
    return_array.append(f'+ {"-" * max_length} +')
    return_array.append(f'| {" " * header_sides}Technicians{" " * header_sides} |')
    return_array.append(f'+ {"-" * max_length} +')
    for name in technician_names:
        return_array.append(f'| {name.ljust(max_length)} |')
    return_array.append(f'+ {"-" * max_length} +')
    return return_array
