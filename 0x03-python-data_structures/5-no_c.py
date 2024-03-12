#!/usr/bin/python3

def no_c(my_string):
    nstring = ""

    for x in my_string:
        if x != 'c' and x != 'C':
            nstring += x
        return nstring
