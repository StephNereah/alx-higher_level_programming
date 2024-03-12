#!/usr/bin/python3
def multiple_returns(sentence):
    lens = len(sentence)

    if (lens == 0):
        new_tuple = (lens, None)
    else:
        new_tuple = (lens, sentence[0])

    return (new_tuple)
