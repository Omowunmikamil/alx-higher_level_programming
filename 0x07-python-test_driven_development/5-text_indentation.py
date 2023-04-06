#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after '.','?',':'
    Arg: text - to be printed
    Raises: TypeError - if text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    
    x = 0
    while x < len(text) and text[x] == ' ':
        x += 1
    
    while x < len(text):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x +=1
            while x < len(text) and text[x] == ' ':
                x += 1
            continue
        x += 1
