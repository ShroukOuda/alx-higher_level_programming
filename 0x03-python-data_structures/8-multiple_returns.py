#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        c = None
    else:
        c = sentence[0]
    t = (len(sentence), c)
    return t
