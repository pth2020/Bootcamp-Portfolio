''' Start of psedo code '''

#request input (name) from user
#store input into variable called "name"
#request input (age) from user
#store input into variable called "age"
#request input (house numer) from user
#store input into variable called "house_number"
#request input (street name) from user
#store input into variable called "street_name"
#output a single statement containing name, age, 
#house number and street name of user

''' End of psedo code '''

#Collect data from user
name = input("Enter your name: ")
#To make sure user enters numbers for age and house_number
try:
  age = input("Enter your age: ")
  house_number = input("Enter your house number: ")
except ValueError:
  print("Invalid input")
  
street_name = input("Enter your street name: ")

print(f"This is {name}. He/she is {age} years old and lives at house number {house_number} on {street_name}.")

