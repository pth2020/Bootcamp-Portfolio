#This program prompts a user to keep inputting numbers.
#It stops once -1 is entered.
#It sums all numbers up with the exception of -1.
#Finally, it outputs the average of the numbers.

#intialisation of numbers
num = 0 
sum1 = 0 
counter = 0  #to keep track of the quantity of numbers entered
average = 0.0

#loop stops once -1 is entered
print("\nAverage of numbers calculator\n")
try:
    while num != -1:
       num = int(input("Enter a number, to stop enter -1.\n"))
       #condition to stop adding '-1' to the sum
       if num != -1:
         sum1 += num
         counter += 1
       elif num == -1 and counter == 0: #if -1 is the only number entered
         counter = 1
       #average of the numbers
       average = sum1/counter 
    
    print("\nAverage of numbers entered: {:.1f}\n".format(average))
       
except ValueError:
   print("Invalid input")
