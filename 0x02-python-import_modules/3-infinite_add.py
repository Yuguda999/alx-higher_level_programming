#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    args.pop(0)

    sum = 0
    for i in args:
        sum += int(i)
    print("{:d}".format(sum))
