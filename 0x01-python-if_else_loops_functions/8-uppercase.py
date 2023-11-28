#!/usr/bin/python3
def uppercase(str):
    upper = ''
    for i in str:
        upper += f'{ord(i) - 32:c}' if ord(i) in range(97, 123) else f'{ord(i) :c}'
    print(upper)
