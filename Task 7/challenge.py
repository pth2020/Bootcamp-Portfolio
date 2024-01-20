#This program works out the final gross annula salary of an employee after pay rise.
#User enters their current annual salary and what percentage pay rise they were awarded
#Program output the a new salary scheme after pay rise.

print("Welcome to salary calculator")
print("\n")

#Runtime error - trying to use a String value as number
current_salary = input("Enter your current salary: £")
#correct line:  current_salary = float(input("Enter your current salary: £"))   

pay_rise_percentage = float(input("Enter percentage for pay rise: (e.g. 3 for 3%) "))

#Logical error - to increase an amount by percentage we use a multipler.
#e.g. for 12% increase we multiply by 1.12
#In the below calculation the  order of operation means that there will be logical error
new_salary = (current_salary * 1 + pay_rise_percentage/100)
#Correct line: new_salary = (current_salary * (1 + pay_rise_percentage/100))

print(f"Current salary: £{current_salary}")
print(f"Percentage pay rise {pay_rise_percentage}%")
print(f"New salary £{new_salary}")
