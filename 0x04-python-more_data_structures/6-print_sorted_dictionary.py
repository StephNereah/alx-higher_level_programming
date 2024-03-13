#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    sort_keys = sorted(a_dictionary.keys())

    for x in sort_keys:
        print("{}: {}".format(x, a_dictionary[x])
