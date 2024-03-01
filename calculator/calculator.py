import math

def scientific_calculator(x,function):
    if function == "sqr_rt":
        return square_root(x)
    elif function == "factorial":
        return fact(x)
    elif function == "abs_value":
        return absolute_value(x)
    elif function == "c_root":
        return cube_root(x)

    
square_root = lambda x: math.sqrt(x)
fact = lambda x: math.factorial(x)
absolute_value = lambda x: abs(x)
cube_root = lambda x: math.cbrt(x)

#calculator - scientific
sqr = scientific_calculator(64,"sqr_rt")
fac = scientific_calculator(5,"factorial")
absolute_v = scientific_calculator(-6,"abs_value")
cb_root = scientific_calculator(125,"c_root")

print(f"Square root of 64  = {sqr}")
print(f"5! = {fac}")
print(f"Absolute value of -6  = |-6| = {absolute_v}")
print(f"Cube root of 125 = {cb_root}")
print()


def basic_calculator(x,operand,y):
    if operand == "+":
        return add(x,y)
    elif operand == "-":
        return subtract(x,y)
    elif operand == "*":
        return multiply(x,y)
    elif operand == "/":
        if y != 0:
            return divide(x,y)
        else:
            return "can not divide by 0!"       


add = lambda x,y: x + y
subtract = lambda x,y: x - y
multiply = lambda x,y: x * y
divide = lambda x,y: x // y 

a = basic_calculator(16,"+",4)
s = basic_calculator(16,"-",4)
m = basic_calculator(16,"*",4)
d = basic_calculator(16,"/",4)


#calculator - basic
print(f"16 + 4 = {a}")
print(f"16 - 4 = {s}")
print(f"16 * 4 = {m}")
print(f"16 / 4 = {d}")
