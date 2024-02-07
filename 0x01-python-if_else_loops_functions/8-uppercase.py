#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        result += "{}".format(chr(ord(char) - (ord('a') - ord('A'))) if 'a' <= char <= 'z' else char

    print(result)
