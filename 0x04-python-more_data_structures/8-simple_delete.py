#!/usr/bin/python3

def simple_delete(a_dictionary: dict, key=""):
    a_dictionary.pop(key) if key in a_dictionary else None
    return a_dictionary
