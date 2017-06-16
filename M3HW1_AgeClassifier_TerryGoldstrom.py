# Age Classifier
# 15 June 2017
# CTI-110 M3HW1 - Age Classifier
# Terry Goldstrom

# Get the person's age
age = int(input("Enter the person's Age "))

# Determine person's category
if age <= 1:
    print('Person is an infant')
elif age < 13:
    print('Person is a child')
elif age < 20:
    print('Person is a teenager')
elif age >= 20:
    print('Person is an adult')
