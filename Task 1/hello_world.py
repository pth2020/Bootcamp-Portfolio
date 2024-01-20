''' start of psedo code '''

#request input (name) from user
#store input into varaible called "name"
#output name
#request input (age) from user
#store input into variable called "age"
#output age 
#output Hello World!

''' end of psedo code '''

name = input("Enter your name: ")
print("Name: ",name) 

try:
  age = input("Enter your age: ")
  print("Age: ",age)
except ValueError:
  print("Invalid input")

print("Hello World!")

