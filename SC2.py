#Name:
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

#Code Here:

'''
#Imperial Version

#Ask the user for the height and weight in inches and pounds
h = int(input("Enter height in inches: "))
w = int(input("Enter weight in pounds: "))

print(f"Your weight is {w} pounds. Your height is {h} inches.")

#Calculate the BMI
BMI = round((w / h ** 2) * 703, 1)
print(f"Your BMI is {BMI}.")

#Tell the user what their classification based on BMI

if BMI < 18.5:
    print("You are underweight.")
elif BMI < 25:
    print("You are normal weight.")
elif BMI < 30:
    print("You are overweight.")
elif BMI >= 30:
    print("You are obese.")
'''


#Metric Version

#Ask the user for the height and weight in inches and pounds
h = float(input("Enter height in meters: "))
w = float(input("Enter weight in kilograms: "))

print(f"Your weight is {w} kilograms. Your height is {h} meters.")

#Calculate the BMI
BMI = round((w / h ** 2), 1)
print(f"Your BMI is {BMI}.")

#Tell the user what their classification based on BMI

if BMI < 18.5:
    print("You are underweight.")
elif BMI < 25:
    print("You are normal weight.")
elif BMI < 30:
    print("You are overweight.")
elif BMI >= 30:
    print("You are obese.")
