#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = a_dictionary.keys()[0]
    for key in a_dictionary.keys():
        max_key = key if a_dictionary[key] > a_dictionary[max_key] else max_key
    return max_key
