#!/usr/bin/python3

def fizzbuzz():

for X in range(100):
    if X % 3 == 0:
        print("Fizz", end=" ")
    elif X % 5 == 0:
        print("Buzz", end=" ")
    elif X % 15 == 0:
        print("FizzBuzz", end=" ")
    else:
        print({X}, end=" ")
