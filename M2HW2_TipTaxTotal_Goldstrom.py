# Tip, Tax, and Total
# 6 June 2017
# CTI-110 M2HW2 - Tip Tax Total
# Terry Goldstrom

# Get the charge for the food.
food_charge = float(input('Enter the charge for the food: '))

# Calculate 18 percent tip
tip = food_charge * .18

# Display Tip amount
print ('The tip amount is $', format (tip, '.2f'))

# Calculate 7 percent sales tax
sales_tax = food_charge * .07

# Display Sales tax amount
print ('The sales tax amount is $', format(sales_tax, ',.2f'))

# Calculate total
total = food_charge + tip + sales_tax

# Display Total Amount
print ('The total amount is $', format(total, ',.2f'))
