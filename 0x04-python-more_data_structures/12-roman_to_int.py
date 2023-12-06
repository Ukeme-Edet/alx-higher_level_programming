#!/usr/bin/python3
def roman_to_int(roman_string):
    i = 0
    vs = {"I": 1, "V": 5, "X": 10, "C": 100, "D": 500, "M": 1000}
    for j in range(len(roman_string)):
        if j > 0 and vs[roman_string[j]] > vs[roman_string[j - 1]]:
            i += vs[roman_string[j]] - 2 * vs[roman_string[j - 1]]
        else:
            i += vs[roman_string[j]]
    return i
