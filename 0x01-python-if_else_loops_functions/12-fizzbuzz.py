#!/usr/bin/python3

def fizzbuzz():
for X in range(1, 101):
    if X % 15 == 0:
        print("FizzBuzz", end=" ")
    elif X % 3 == 0:
        print("Fizz", end=" ")
    elif X % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(X, end=" ")
