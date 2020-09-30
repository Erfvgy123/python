# 1st App - Calculator
# Started: 09/12/20
# Last Updated: 09/29/20

import math


# Basic Calculator

def basic_calc(response):
    while(response != "q"):

        if response == "add":
            num_one = int(input("Enter first number to add:"))
            num_two = int(input("Enter second number to add:"))
            print("Addition:")
            print(num_one + num_two)

        if response == "subtract":
            num_one = int(input("Enter first number to subtract:"))
            num_two = int(input("Enter second number to subtract:"))
            print("Subtraction:")
            print(num_one - num_two)

        if response == "multiply":
            num_one = int(input("Enter first number to multiply:"))
            num_two = int(input("Enter second number to multiply:"))
            print("Multiplication:")
            print(num_one * num_two)

        if response == "division":
            num_one = int(input("Enter first number to divide:"))
            num_two = int(input("Enter second number to divide:"))
            print("Division:")
            print(num_one / num_two)


# Advanced Calculator

def advanced_calc(response):
    while(response != "q"):

        if response == "exponents":
            number = int(input("Enter the number"))
            exponent = int(input("Enter the exponent"))
            print("Exponent: ")
            print(math.pow(number, exponent))

        if response == "sqaureroot":
            num_one = int(input("Enter the number for its square root"))
            print("Square root: ")
            print(math.sqrt(num_one))


# Choose basic or advanced type of calculator

calcType = input("Select the type of calculator to use (Basic or Advanced) ")
currentCalc = None


def choose_calc(calcType):

    if calcType == "Basic":
        response = input(
            "What operation would you like to perform? (Add, Subtract, Divide, Multiply) ")
        currentCalc == "Basic"
        print("Loading basic calculator...")
        basic_calc(response)

    elif calcType == "Advanced":
        response = input(
            "What operation would you like to perform? (Exponents or Square Roots) ")
        currentCalc == "Advanced"
        print("Loading advanced caluclator...")
        advanced_calc(response)

    else calcType != "Basic" or "Advanced":
        print("Invalid response")
