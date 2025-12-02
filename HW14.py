#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW14

import random
#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
for i in range(5, 0, -1):
    print(i)
else:
    print("Hello World!")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for j in range(1,31):
    if j % 2 == 0:
        print(j)
    else:
        continue
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for k in range(1,31):
    if k % 3 == 0:
        continue
    else:
        print(k)
#4. Create a for loop that prints 5 different animals from a list.
animals = ["dogs", "monkeys", "penguins", "pigs", "donkeys"]
for l in animals:
    print(l)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for m in input("Enter a word: ")[::-1]:
    print(m)
#6. Create a list containing 10 integers of your choice and print the list.
num_list_random = [random.randint(1,10),random.randint(1,10),random.randint(1,10),
                   random.randint(1,10),random.randint(1,10),random.randint(1,10),
                   random.randint(1,10),random.randint(1,10),random.randint(1,10),
                   random.randint(1,10)]
print(num_list_random)
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for n in num_list_random:
    if n % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1

print(f"Even numbers: {evenNumbers}, Odd numbers: {oddNumbers}")
#9. Create a variable that asks the user for an integer and an empty integer variable.
num_prompt = int(input("Enter a number: "))
o = 1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for p in range(1, num_prompt + 1):
    o *= p

print(o)
