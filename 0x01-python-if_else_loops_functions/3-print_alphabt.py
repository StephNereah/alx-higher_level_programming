#!/usr/bin/python3

for C in range(97, 123):
    if chr(C) not in 'eq':
        print("{}".format(chr(C)), end="")
