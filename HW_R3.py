#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW-R3
import random

#1. import random and print "Hello World!"
print("Hello World!")
#2. Create three variables that each randomly generate an integer between 1 and 10, print each number on the same line.
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
print(a,b,c)
#3. Create a list containing 5 strings listing 5 colors.
color_list = ["Red", "Yellow", "Green", "Blue", "Purple"]
#4. Use a function to randomly choose one of the 5 colors from the list and print the result.
print(random.choice(color_list))
#5. Create an if statement that determines which of the three variables from #2 is the lowest.
if a == b == c:
    print("They are all the same")
elif b <= a and b <= c:
    print(f"{b} is the lowest")
elif c <= b and c <= a:
    print(f"{c} is the lowest")
elif a <= b and a <= c:
    print(f"{a} is the lowest")

