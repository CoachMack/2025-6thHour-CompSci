#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Try Except


#This is a Try Except catch. It initially tries to do one piece of code and in the case of an error,
#it does whatever code set under the except. This allows for the code to continue on when there is an
#error which can help with debugging.
try:
    print(x)
except:
    print("Hello World!")


#You can define which exceptions to check for. This is useful for instances when there are different
#possible errors that can occur. In this example, if the user inputs zero (0), it gives a divide by
#zero error. If the user inputs something other than an integer, it gives a Value Error. If it's
#something else that might show up unexpectedly, you can put a general 'except' and anything else
#will go there.
try:
    num_div = int(input("Give me an integer: "))
    print(100/num_div)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Value Error. Needs to be an integer!")
except:
    print("Unknown error.")

#There is also finally which does whatever code is under it regardless of if an exception is caught
#or not. Think of it like an else statement but it just does that part of the code no matter what.
try:
    print(y)
except:
    print("Something went wrong!")
finally:
    print("This is the end of the Try Except!")

#You can also raise exceptions that will throw a big red error and end the code anyway but you can
#customize what the error says to help with debugging.
i = -1

if i < 0:
    raise Exception("You can't bet, you don't have money!")


#You can put raised exceptions inside of except blocks. Both concepts work in tandem.
try:
    k = int(input("Give me an integer"))
    print(k)
except:
    raise ValueError("It needs to be an integer!")



