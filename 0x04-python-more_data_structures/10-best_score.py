#!/usr/bin/python3

def best_score(a_dictionary):
    max_score = 0
    if a_dictionary is None:
        return None
    for key, value in a_dictionary.items():
        if value > max_score:
            best_key = key
            max_score = value
    return best_key
