#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    words = sorted(a_dictionary)

    for x in words:
        print("{}: {}".format(x, a_dictionary[x]))
