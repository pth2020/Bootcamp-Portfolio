"""
Psedo code starts here

create a variable called num1
store a float value into num1
create a variable called num2
store an integer value into num2
create a variable called num3
store an integer value into num3
create a variable called string1
store an integer inside a double/single quote into string1 
convert num1 into integer
convert num2 into float
convert num3 into String
convert string1 into an integer
output num1, num2, num3 and string1 before/after conversion    

Psedo code ends here    
"""


num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

#variables before conversion
print("\nVariables before conversion...\n")
print("num1:",num1,type(num1))
print("num2:",num2,type(num2))
print("num3:",num3,type(num3))
print("string1:",string1,type(string1))

#casting (converting) variables
num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1)

#variables after conversion
print("\nVariables after conversion...\n")
print("num1:",num1,type(num1))
print("num2:",num2,type(num2))
print("num3:",num3,type(num3))
print("string1:",string1,type(string1))
