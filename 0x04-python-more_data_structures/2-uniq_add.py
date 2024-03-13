#!/usr/bin/python3

def uniq_add(my_list=[]):
    newlist = set()

    for x in my_list:
        newlist.add(x)

    return sum(newlist)
