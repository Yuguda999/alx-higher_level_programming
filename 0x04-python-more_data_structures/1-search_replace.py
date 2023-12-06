#!/usr/bin/python3

def search_replace(my_list, search, replace):
    copied_list = []
    for i in my_list:
        if i == search:
            i = replace
        copied_list.append(i)

    return copied_list
