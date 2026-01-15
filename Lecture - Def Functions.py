#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Def Functions
import random

#This is a def function. These are custom functions designed to "segment" and organize your code in
#Python! You can also use them to reuse the same code but with different sets of data (called "arguments")
#in a way that doesn't require copying and pasting said same code over and over again.
def hello_world():
    print("Hello World!")

#This is how you "call" a function.
hello_world()


#You can place variables to be used for arguments inside of where the def function is created.
#This allows you to assign a value to a variable using an argument and so it will use that data
#wherever that variable is used inside of the function.
def class_name(name):
    print(name, "is in 6th Hour!")

#In this case, we put the value "Ally" as our argument and so it set the name variable to = "Ally".
#So as it is written, it will print out "Ally is in 6th hour."
class_name("Ally")
class_name("Ethan")


#You can make multiple variables and assign multiple arguments to each one. When written on
#their own, arguments are assigned in order, so the first number in the argument would be assigned to
#a and the second to b.
def addition(a,b):
    c = a + b
    print(c)

addition(20, 30)


#Using a single asterisk in front of the variable, you can turn all of your arguments into a list,
#and pull their values like you would a normal list.
def student_list(*student):
    print("The 5th Student is:", student[4])

student_list("Alaya", "Ally", "GREG", "Shane", "Carlos", "Tristan", "Connor", "Eli", "Ethan")


#You can also do the same thing and make it a dictionary by using two asterisks in front of the variable.
def student_info(**stu_info):
    print("The Student's last name is:", stu_info["lname"])
    print("They are a", stu_info["grade"])
    print("Their favorite game is", stu_info["vidya"])

#Just be sure to give every value a keyword in front of it like you would with a dictionary.
student_info(fname = "Carlos", lname = "Lopez", grade = "freshman", vidya = "Fortnite")


#This is a quick and dirty example of how you can use def functions to repeat specific kinds of code.
def coin_flip():
    player_call = int(input("1 for heads, 2 for tails"))
    coin_flip_result = random.randint(1,2)

    if coin_flip_result == player_call:
        print("You win!")
    else:
        print("You lose!")
    repeat_game()

#Note here how you can call the function inside of itself to repeat the code.
def repeat_game():
    player_input = input("Do you want to play again? Y/N")

    if player_input == "Y" or player_input == "y":
        coin_flip()
    else:
        print("Thank you for playing!")

coin_flip()


#You can also change variables outside of the def function using the "global" command. By establishing
#the variable outside the function and then "calling" it inside, you can change the variable in any way
#you want and it will change the value outside of the function too. This is a good way to "count"
#results inside of the def function.
x = 1

def make_x_2():
    global x
    x = 2

def print_new_x():
    print(x)

#If you don't call any function that changes the variable globally, any other function that
#uses the variable will use its original value, NOT the changed value.
make_x_2()
print_new_x()
