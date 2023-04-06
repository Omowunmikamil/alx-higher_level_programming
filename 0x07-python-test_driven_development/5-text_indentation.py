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
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1
    
    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c +=1
            while c < len(text) and text[c] == ' ':
                c += 1
                continue
            c += 1
