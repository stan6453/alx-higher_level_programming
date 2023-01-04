#!/usr/bin/python3
"""Text indent module."""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of thesecharacters.

    '.', '?' and ':'.
    """
    """Tests"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    """Operation Logic."""
    new_text = ""
    new_line = False
    for character in text:
        if character in [".", "?", ":"]:
            print(character + "\n\n", end="")
            new_line = True
        else:
            if new_line and character in [" ", '\t']:
                new_line = False
                continue
            new_line = False
            print(character, end="")
