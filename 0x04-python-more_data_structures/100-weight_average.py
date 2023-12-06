#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = []
    denominator = []
    for tup in my_list:
        a, b = tup
        numerator.append(a*b)
        denominator.append(b)
    return sum(numerator) / sum(denominator)
