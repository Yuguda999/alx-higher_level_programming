#!/usr/bin/python3
for i in range(100):
    print(f'{i:d}'.rjust(2, '0'), end='\n' if i == 99 else ',')
