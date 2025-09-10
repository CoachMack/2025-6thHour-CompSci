#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Random


#This is the random library. This allows us to do random choice and random number generation
#in python. The main three I want you to learn about is randint, choice, and shuffle.
import random

#The function "randint" provides a random integer between a range (X, Y) where
#X is the bottom of the range and Y is the top of the range.

#REMINDER: ALL functions from a library need to call the library to work. In this example,
#before we write "randint" we need to write "random."
d10 = random.randint(1,10)
print(d10)


#randint is ultimately an integer so you can do math with them accordingly.
d20 = random.randint(1,20)
d6 = random.randint(1,6)
print(f"{d20}, {d6}")
print(d20 + d6)
print(d20 - d6)


#By that same logic, you can dump a bunch of randint into a list and it will generate a list of
#integers for you every time you run the code.
rand_num_list = [random.randint(1,10), random.randint(1,10), random.randint(1,10),
                 random.randint(1,10), random.randint(1,10), random.randint(1,10),
                 random.randint(1,10), random.randint(1,10), random.randint(1,10), ]
print(rand_num_list)


#The function "choice" randomly chooses from a list just like one would blindly choose
#a colored ball from a bag or something of that nature.
class_num_list = [4, 1111, 1, 2, 21, 25, 42, 80, 67, 6, 8, 323, 11]
print(random.choice(class_num_list))


#The function "shuffle", just like your spotify playlist, randomly shuffles the objects inside
#of a list and if you were to print the whole list, it would be in a different order every time
#you run the code.
random.shuffle(class_num_list)
print(class_num_list)

