'''
This program calculates:
1. The amount of interest a customer earns on their investment.
   Customer enters the initial amount of investment(principal),
   the interest rate(percentage), the number of years to invest,
   and the type of interest (simple or compound)
   Program outputs the amount customer earns after specified years.
2. The amount to pay on a home loan
   Customer enters present value of house, interest rate(percentage)
   and the number of months they prefer to repy the loan
   Program outputs the amount to rey each month.

'''

print("\n********************************************")
print("Welcome to investment and bond calculator ")
print("********************************************")

def compute_investment():
   #validators for investment selected option and entered values
   valid_investment_option = True 
   valid_investment_values = True 
   investment_type = '' #simple or compound

   #intilise investment values   
   investment_amount= 0.0
   investment_principal = 0.0
   investment_rate = 0.0
   investment_years = 0

   #provide user with investment options to choose from - simple or compound
   print("\nNow select the type of investment:\n")
   print("1. Simple Investment")
   print("2. Compound Investment")

   selected_investment_option = 0

   try:
      selected_investment_option = int(input("\nMenu choice: (1 or 2): "))
      while selected_investment_option < 1 and selected_investment_option > 2:
         print("You can only select option 1 or 2.")
         selected_investment_option = int(input("\nMenu choice: (1 or 2): "))         
   except ValueError:
      valid_investment_option = False
      print("Invalid input..") 
   

   #User enters values for principal, interest rate and number of years and validity of the values are checked 
   if valid_investment_option:
      try:
         investment_principal = float(input("\nEnter the amount of money you want to deposit: £"))
         investment_rate = float(input("\nEnter the interest rate (e.g. 2 for 2%): " )) 
         investment_years = int(input("\nEnter the number of years you want to invest your money for: "))
         #checking validity of entered values
         if investment_principal <= 0 or investment_rate <= 0 or investment_years < 1:
            raise Exception("Incorrect value for principal or interest rate or number of years entered.")
            valid_investment_values = False           
      except ValueError:
         print("Invalid input")

   
   if valid_investment_values:
      if selected_investment_option == 1: 
         #calculate the amount of investment with simple interest 
         investment_amount = investment_principal*(1 + (investment_rate/100)*investment_years)
         investment_type = "Simple Investment"
      elif selected_investment_option == 2: 
         #calculate the amount of investment with compound interest 
         investment_amount = investment_principal*(1 + investment_rate/100)**investment_years
         investment_type = "Compound Investment"

   if valid_investment_values and valid_investment_option:
      print()
      print("Outcome")
      print("*************************************************************")
      print(f"Investment type: {investment_type}")
      print(f"Amount invested: £{round(investment_principal,2)}") #rounding value to 2 decimal places
      print(f"Interest rate {investment_rate}%")
      print(f"Number of years invested: {investment_years} years")
      print(f"Current balance: £{round(investment_amount,2)}")
      print("*************************************************************")
   
def compute_bond():
   #validator for entered bond values
   valid_bond_values = True
   
   #initialise bond values
   bond_value = 0.0
   bond_interest_rate = 0.0
   bond_repayment_months = 1
   bond_monthly_repayment_amount = 0.0

   print("Bond calculation...")
   try:
      bond_value = float(input("\nEnter the value of the house: £"))
      bond_interest_rate = float(input("\nEnter the bond's interest rate (e.g. 2 for 2%): " )) 
      bond_repayment_months = int(input("\nEnter the number of months you want to repay the bond: "))
      #checking validity of entered values
      if bond_value <= 0 or bond_interest_rate <= 0 or bond_repayment_months < 1:
            valid_bond_values = False         
            raise Exception("Incorrect bond value, bond interest rate or number of repayment months.")
   except ValueError:
      print("Invalid input.")   
   

   if valid_bond_values:
         #monthly interest rate - annual rate divided by 100 and then divide by 12 yields monthly rate
         i = ((bond_interest_rate/100)/12 )
         p = bond_value
         n = bond_repayment_months
         bond_monthly_repayment_amount = (i * p)/(1 - (1 + i)**(-n))
         print()
         print("Outcome")
         print("*************************************************************")
         print(f"Present value of house: £{round(bond_value,2)}")
         print(f"Bond interest rate {bond_interest_rate}%")
         print(f"Number of repayment months: {bond_repayment_months} months")
         print(f"Amount to repay each month: £{round(bond_monthly_repayment_amount,2)}")
         print("*************************************************************")


print("-------------------------------------------------------------------------------------")
print("\ninvestment - to calculate the amount of interest you will earn on your investment.")
print("\nbond - to calculate the amount you'll have to pay on a home loan.")
print("-------------------------------------------------------------------------------------")
print("\nEnter either \'investment\' or \'bond' from the menu above to proceed.")

selected_option = ''

try:
   selected_option = input("\nEnter your option: ").lower()
   if selected_option != 'investment' and selected_option != 'bond':
         raise Exception("Invalid entry")  
except:
   print("Invalid entry")

if selected_option == 'investment': #call compute_investment() function
   compute_investment()
elif selected_option == 'bond': #call compute_bond() function
   compute_bond()   
