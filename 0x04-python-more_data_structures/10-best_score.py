#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        Max = 0
        Key = ''
        for key, value in a_dictionary.items():
            if value > Max:
                Max = value
                Key = key
        return Key
    return None
