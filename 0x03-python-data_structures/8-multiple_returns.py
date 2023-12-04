#!/usr/bin/python3

def multiple_returns(sentence):
    """
    returns a tuple with the length of a string and its first character
    Args:
        sentence - string
    Return:
        (length, first)
    """
    first_letter = sentence[0] if sentence else None
    return (len(sentence), first_letter)
