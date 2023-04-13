#!/usr/bin/python3
"""Module that reads a text file"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf8") as file:
        text = file.read()
        print(text, end="")
