# Kilometer Converter
# 27 June 2017
# CTI-110 M5T1_KilometerConverter
# Terry Goldstrom

# This program converts kilometers to miles.
CONVERSTION_FACTOR = 0.6214

# The main function gets a distance in kilometers and calls
# the show_miles function to convert it.
def main ():
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles(kilometers)

# The show_miles function converts the paramenter km from
# kilometers to miles and displays the result.
def show_miles(km):
    # Calculate miles.
    miles = km * CONVERSTION_FACTOR

    # Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')
                                                           
# Call the main function.
main()
