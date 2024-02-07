#!/usr/bin/python3

for F in range(10):
    for S in range(F + 1, 10):
        print("{}{}".format(F, S), end=", " if (F != 8 or S != 9) else "\n")
