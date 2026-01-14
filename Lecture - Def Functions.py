#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Def Functions
import random


def hello_world():
    print("Hello World!")

hello_world()


def class_name(name):
    print(name, "is in 6th Hour!")

class_name("Ally")
class_name("Ethan")

def addition(a,b):
    c = a + b
    print(c)

addition(20, 30)


def student_list(*student):
    print("The 5th Student is:", student[4])

student_list("Alaya", "Ally", "GREG", "Shane", "Carlos", "Tristan", "Connor", "Eli", "Ethan")

def student_info(**stu_info):
    print("The Student's last name is:", stu_info["lname"])
    print("They are a", stu_info["grade"])
    print("Their favorite game is", stu_info["vidya"])

student_info(fname = "Carlos", lname = "Lopez", grade = "freshman", vidya = "Fortnite")


def coin_flip():
    player_call = int(input("1 for heads, 2 for tails"))
    coin_flip_result = random.randint(1,2)

    if coin_flip_result == player_call:
        print("You win!")
    else:
        print("You lose!")
    repeat_game()

def repeat_game():
    player_input = input("Do you want to play again? Y/N")

    if player_input == "Y" or player_input == "y":
        coin_flip()
    else:
        print("Thank you for playing!")

coin_flip()


x = 1

def make_x_2():
    global x
    x = 2

def print_new_x():
    print(x)

make_x_2()
print_new_x()
