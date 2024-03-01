import math

def scientific_calculator(function):
    if function == "square root":
        return square_root
    elif function == "factorial":
        return factorial
    elif function == "absolute_value":
        return abs_value

    
square_root = lambda x: math.sqrt(x)
factorial = lambda x: math.factorial(x)
abs_value = lambda x: abs(x)

#calculator - scientific
print(f"Square root of 64  = {square_root(64)}")
print(f"5! = {factorial(5)}")
print(f"Absolute value of -6  = |-6| = {abs_value(-6)}")
print()


def basic_calculator(x,operand,y):
    if operand == "+":
        return add
    elif operand == "-":
        return subtract
    elif operand == "*":
        return multiply
    elif operand == "/":
        if y != 0:
            return divide
        else:
            return "can not divide by 0!"       


add = lambda x,y: x + y
subtract = lambda x,y: x - y
multiply = lambda x,y: x * y
divide = lambda x,y: x // y 

#calculator - basic
print(f"16 + 4 = {add(16,4)}")
print(f"16 - 4 = {subtract(16,4)}")
print(f"16 * 4 = {multiply(16,4)}")
print(f"16 / 4 = {divide(16,4)}")
