# Random Number File Writer
# 4 July 2017
# CTI-110 M6HW1 - Random Number File Writer
# Terry Goldstrom

# Import the random module
import random

# Open file for writing and assign it to the variable random_numbers
random_numbers = open("Random.txt", "w" )

# Get the desired of random numbers to be generated
qty_numbers = int(input('Input how many random numbers should be written to the file:  '))
print('Your list of random numbers are: ')

# Create a loop to generate the random numbers in the quantity specified
for count in range (qty_numbers):
    number = random.randint(1,500)
    # Print the list of random numbers
    print(number)

    random_numbers.write(str(number)+ '\n')

# Close the file.
random_numbers.close()

# Let user know the numbers have been written to the file name.
print('Your list of random numbers have been written to the file named')
print('Random.txt')
