#!/usr/bin/python3

def no_c(my_string):

    n = 0

    nstr = my_string[:]

    for i in range(len(my_string):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            nstr = nstr[:(i - n)] + my_string[(i + 1):]
            n += 1
    return (nstr)
