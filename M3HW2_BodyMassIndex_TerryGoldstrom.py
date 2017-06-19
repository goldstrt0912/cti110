# Body Mass Index
# 15 June 2017
# CTI-110 - Body Mass Index
# Terry Goldstrom

# Get users height and weight
height = float(input("Input your height in inches: "))
weight = float(input("Input your weight in pounds: "))

# Calculate BMI
bmi=weight*703/(height*height)
print("Your body mass index is ", format(bmi, ",.1f"))

#Classify Users category
if bmi <= 18.5:
    print('You are underweight')
elif bmi <= 24.9:
    print('You are at a normal weight')
elif bmi <= 29.9:
    print('You are overweight')
elif bmi >= 30.0:
    print('You are obese')
