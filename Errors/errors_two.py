# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #Runtime error (NameError) - undefined data type
animal_type = "cub"
number_of_teeth = 16

#Logical error - formatting of data missing, animal_type and number_of_teeth in wrong orders
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"


print(full_spec) #Syntax error - brackets missing


'''

This example program is meant to demonstrate errors.
 
There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = Lion
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"

print full_spec

'''
