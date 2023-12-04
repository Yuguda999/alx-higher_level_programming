#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    finds all multiples of 2 in a list
    Args:
        my_list - list default empty
    Return:
        list
    """
    new_list = []
    for i in my_list:
        new_list.append(True) if i % 2 == 0 else new_list.append(False)
    return new_list
