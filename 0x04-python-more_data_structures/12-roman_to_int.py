#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = 0
    p = 0
    if isinstance(roman_string, str) and roman_string:
        for c in reversed(roman_string):
            if val[c] >= p:
                r += val[c]
            else:
                r -= val[c]
            p = val[c]
    return r
