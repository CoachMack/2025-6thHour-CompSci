#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW16
import random


#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello world!")
#2. Create a def function that calculates the average of three numbers (set the 3 numbers as your arguments).
def average(a,b,c):
    avg = (a + b + c)/3
    print(avg)

def average_list(*num_list):
    avg = sum(num_list)/len(num_list)
    print(avg)


#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animals(*animal_list):
    print(animal_list[2])

#4. Create a def function that loops from 1 to the number put in the argument.
def loop(end):
    for i in range(1, end + 1):
        print(i)
#5. Call all of the functions created in 1 - 4 with relevant arguments.
hello_world()
average(1,2,3)
average_list(5,6,7,8)
animals("Monkey", "Tiger", "Dog", "Cat", "Pangolin", "Fox")
loop(5)
#6. Create a variable x that has the value of 2. Print x
x = 2
print(x)
#7. Create a def function that multiplies the value of x by a random number between 1 and 5.
def x_times_random():
    global x
    x = x * random.randint(1,5)
x_times_random()
#8. Print the new value of x.
print(x)
