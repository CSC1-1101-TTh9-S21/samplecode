# getting input from user
year = int(input("What is your year of graduation? "))
major = input("What is your major? ")

# setting priority to -1
# if it comes back at -1 at the end, we know something
# went really wrong!
priority = -1

# using nested if statements
if year==2021:
    if major=="CS":
        priority=1
    else:
        priority = 3
elif year == 2022:
    if major=="CS":
        priority = 2
    else:
        priority = 5
elif year == 2023:
    if major == "CS":
        priority = 4
else:
    priority = 6

print("Your priority is {}".format(priority))

# using and operator
if year==2021 and major=="CS":
    priority =1
elif year== 2022 and major=="CS":
    priority = 2
elif year == 2021:
    priority = 3
elif year==2023 and major=="CS":
    priority = 4
elif year==2022:
    priority = 5
else:
    priority = 6
    
print("Your priority is {}".format(priority))
