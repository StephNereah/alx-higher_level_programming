#!/usr/bin/python3

def uppercase(str):
    for S in (str):
        print("{}".format(chr(ord(S) - (ord('a') - ord('A'))) if 'a' <= S <= 'z' else S), end="")
    print()
