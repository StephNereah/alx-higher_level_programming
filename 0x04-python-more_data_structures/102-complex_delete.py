#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    copy_d = a_dictionary.copy()
    for key1, value1 in copy_d.items():
        if value1 == value:
            del a_dictionary[key1]
    return a_dictionary
