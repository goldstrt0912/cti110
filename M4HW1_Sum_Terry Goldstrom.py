# Sum of Numbers
# 20 June 2017
# CTI-110 M4HW1 - Sum of Numbers
# Terry Goldstrom

# Initialize the accumulator
total = 0

# Get the first number
number = float(input('Please enter the first number (negative to quit): '))

# Number must be greater than -1
while number > -1:

    # Add positive numbers
    total = total + number

    # Continue adding positive numbers, until negative number is entered
    number = float(input('Please enter the next number (negative to quit): '))

# Display total of all positive numbers
print('The sum of all the numbers you enter is', total)
