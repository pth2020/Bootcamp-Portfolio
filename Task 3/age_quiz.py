print("Welcome to age quiz")
print()

#to check if user's input is valid
age_valid = False

#checking for exception
try :
    age = int(input("Enter your age: "))
    if age > 0:
        age_valid = True
except ValueError: #if a user enters non digit (non-integer)
    print("Invalid input!")
   
#Various age scenarios
if age_valid:
    if age > 100:
        print("Sorry, you're dead.")
    elif age >= 65:
        print("Enjoy your retirement!")
    elif age >= 40:
        print("You're over the hill.")
    elif age == 21:
        print("Congrats on your 21st!")
    if age < 13:
        print("You qualify for the kiddie discount.")
    else:
        print("Age is but a number.")
