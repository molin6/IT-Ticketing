from flask import jsonify

def print_technician_names(technician_names):
    names = []
    for name in technician_names:
        names.append({
            "name": name
        })
    return jsonify(names)

