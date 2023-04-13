#!/usr/bin/python3
"""Module that crates an object"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a "JSON file"
    """
    

    with open(filename, encoding="utf-8") as file:
        return json.load(file)
