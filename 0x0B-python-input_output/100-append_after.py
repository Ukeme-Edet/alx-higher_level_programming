#!/usr/bin/python3
"""
A function that inserts a line of text to a file, after each line containing a
specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific
    string
    """
    with open(filename, mode="r+", encoding="utf-8") as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            if search_string in line:
                lines.insert(i + 1, new_string)
            i += 1
        f.seek(0)
        f.writelines(lines)
