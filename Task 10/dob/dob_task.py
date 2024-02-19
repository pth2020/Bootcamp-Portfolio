import re

# -- Intialising names list
names = [] 

# -- Initialising date of birth (dob) list
dob = []

# -- Reading dob.txt file
with open("dob.txt",'r') as file:
    for line in file:
        # -- finding the first digit in a line to separate name from dob using regex
        # -- example, John Smith 24 Feb 2000
        match_digit = re.search(r'\d',line)

        # -- Slice line into name and dob
        names.append(line[:match])
        dob.append(line[match:].strip())
        
print("Name")
for i in range(len(names)):
    print(names[i])
print()
print("Birthdate")
for j in range(len(dob)):
    print(dob[j])
