#!/usr/bin/python3
"""load add save"""

import sys


def michael():
    """a script that adds arguments to a python file"""

    save_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_json_file = __import__("6-load_from_json_file").load_from_json_file

    file = "add_item.json"
    json_list = []

    try:
        load_json_file(file)
    except FileNotFoundError:
        json_list = []

    json_list.extend(sys.argv[1:])
    save_file = save_json_file(json_list, file)
    return save_file


michael()
