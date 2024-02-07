#!/usr/bin/python3

for X in range(0, 100):
    print("{:02d}".format(X), end=", " if X < 99 else "\n")
