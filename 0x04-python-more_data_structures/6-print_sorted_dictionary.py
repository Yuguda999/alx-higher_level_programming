#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sortedkeys = sorted([key for key in a_dictionary.keys()])
    for key in sortedkeys:
        print(f"{key:s}: {a_dictionary.get(key)}")
