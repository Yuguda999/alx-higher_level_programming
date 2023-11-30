#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv
    args.pop(0)
    args_length = len(args)
    first_line = "{:d} argument".format(args_length)
    if args_length == 0:
        first_line += "s."
    elif args_length == 1:
        first_line += ":"
    else:
        first_line += "s:"
    print(first_line)

    for i, arg in enumerate(args):
        print("{:d}: {:s}".format(i+1, arg))
