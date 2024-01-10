#!/usr/bin/python3
"""
A function that creates an Object from a “JSON file”
"""
import json


def load_from_json(filename):
    """
    Creates an Object from a “JSON file”
    """
    with open(filename, "r") as f:
        return json.load(f)
