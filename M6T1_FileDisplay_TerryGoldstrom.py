# File Display
# 4 July 2017
# CTI-110 M6T1 - File Display
# Terry Goldstrom

# Open the file.
myfile = open('numbers.txt', 'r')

# Read and display the file's contents.
for line in myfile:
    number = int(line)
    print(number)
    
# Close the file.
myfile.close()
