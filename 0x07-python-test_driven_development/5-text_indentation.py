#!/usr/bin/python3
"""
A module that defines a function that prints a text with 2 new lines after each
of these characters: '.', '?' and ':'
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?' and
    ':'
    Args:
        text (str): The text to print
    Raises:
        ypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    lines, line = [], ""
    for i in range(len(text)):
        line += text[i]
        if text[i] in ".?:":
            lines.append(line.strip())
            lines.append("")
            line = ""
    if line.strip():
        lines.append(line.strip())
    [print(line) for line in lines]
