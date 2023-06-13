#!/usr/bin/env python3

def greet_programmer():
    print("Hello Programmer")

greet_programmer()

def greet(name):
    print(f"Hello, {name}")

greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}")

greet_with_default("Sunny")

def add(num1, num2):
    print(num1 +num2)

add(1,2)

def halve(number):
    if type(number) != int:
        print("null")
    else:
        print(number / 2)

halve(4)