#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Syntax and Variables

#This is a print function. It prints out exactly what is inside the parentheses.
print("Hello 6th Hour Class")

#You can print out two different things using either a plus(+) or a comma(,). Typically it is best
#to print things out with a comma. A plus might add together two different numbersd instead of
#printing them out separately.
print("Hello 6th Hour Class. " + "How are you today?")
print("Hello 6th Hour Class.", "How are you today?")

#This is a variable. Variables are where you can store specific values to use for things. Typically,
#variables store one of three types of values: numbers, words, and boolean. Every variable is read
#by the program as variable_name = "variable value" so keep that in mind. The name ALWAYS comes first.
class_greetings = "Hello 6th Hour Class. How are you today?"

#You can print the value of variables by putting the name of the variable inside of a print statement.
print(class_greetings)

#This is an input function. Input functions will pause and wait for the user to enter their own data
#before continuing. Inside the parentheses, you can add something to specify what you want the user to type.
#Whatever the user types will be the value of that variable. Remember, an input function NEEDS to be equal
#to a variable to store the value.
studentName = input("Insert name of student here: ")

print(studentName)


#You can also put functions inside of other functions for various reasons. In this example, we put an input
#function inside of an int function so that it will only accept integers as a valid user response.
#If the user were to put a string (or word) as the response, the code would throw an error.
guessing_game_number = int(input("Give me a number between 1 and 10: "))

print(guessing_game_number)


#Python reads code line by line starting at line 1. You can manually change the value of a
#variable later on for whatever reason.
class_greetings = "I have changed the value of class_greetings."

print(class_greetings)
