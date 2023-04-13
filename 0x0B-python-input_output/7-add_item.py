#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


import sys

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except:
    my_list = []
my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
