# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #Syntax error - brackets missing
print ("\n") #Syntax error - incorrect indentation and brackets missing

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" #syntax error - wrong indentation
age = int(age_Str) #sysntax error - wrong indentation
print(f"I'm {age} years old.") #syntax error - wrong indentation
                                #Runtime error (TypeError) - age needs to be cast into String inside print() or format{} needs to be used
# Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = age + int(years_from_now) #Runtime error(TypeError),  + will be wrong operand for int and String data types, 
                                        #years_from_now needs to be cast to int, + will then be addition

print(f"The total number of years: {total_years}") #Syntax error (missing brackets)
                                                  #Logical error - total_years is int and as such it should be formatted.
                                                                # + is concatenating and total_years becomes a string                                                                   
                                                   

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years + 0.5) * 12 #Runtime error (NameError) - 'total' undefined variable
                                        #Logical error - 6 months (0.5 years) not added to total_years
print(f"In 3 years and 6 months, I'll be {int(total_months)} months old") #Syntax error (missing brackets)
                                                                          #Logical error - total_months needs to be cast to int

#HINT, 330 months is the correct answer

'''
print "Welcome to the error program"
    print "\n"

    # Variables declaring the user's age, casting the str to an int, and printing the result
    age_Str == "24 years old" 
    age = int(age_Str) 
    print("I'm" + age + "years old.")

    # Variables declaring additional years and printing the total years of age
    years_from_now = "3"
    total_years = age + years_from_now

print "The total number of years:" + "answer_years"

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total * 12
print "In 3 years and 6 months, I'll be " + total_months + " months old"

#HINT, 330 months is the correct answer

