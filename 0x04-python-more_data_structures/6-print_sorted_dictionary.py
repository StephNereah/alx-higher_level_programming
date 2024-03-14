#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    sort_keys = list(a_dictionary.keys())
    sort_keys.sort()
    
    for x in sort_keys:
        print("{}: {]".format(x, a_dictionary.get(x)))
