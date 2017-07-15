# Random Number File Reader
# 4 July 2017
# CTI-110 M6HW2 - Random Number File Reader
# Terry Goldstrom

# Open file to read file
random_numbers = open('random.txt', 'r')
# Variable to store sum
number = 0
# Variable to count numbers
total = 0

# Loop use to read all numbers from text file.
for line in random_numbers.readlines():
        # Lists numbers read from text file.
        print(line)
        # Calculate all random numbers from text file.
        total = total+int(line)
        # Determine total of numbers read from text file.
        number +=1
        
# Display Sum of the numbers
print("The Sum of the numbers = "+str(total))
# Display total amount of numbers read
print("The total amount of numbers read are "+str(number))
