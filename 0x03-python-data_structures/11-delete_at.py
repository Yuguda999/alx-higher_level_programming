#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    deletes the item at a specific position in a list
    Args:
        my_list - list default empty
        idx - integer list index
    Return:
        list
    """
    if -1 < idx < len(my_list):
        del my_list[idx]
    return my_list
