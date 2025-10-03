#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Conditional Statements

import random

#This section is a conditional statment (AKA an "if then" or "if else" statement).
#These are used for giving your code specific directions based on whatever rules you
#set for it. There are three different types of conditional statements.

#if = Check to see if this condition is valid.
#elif = Short for "else if". Check to see if this condition is valid if the first isn't.
#else = If no other condition is valid, do this.

#Often you have conditional statements being compared using logical conditions from mathematics.

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

coin = random.randint(0,1)

#If you only have two possible results to check conditions, simply using an if else is fine.
if coin == 0:
    # YOU MUST INDENT EVERYTHING YOU WANT TO DO WITHIN AN IF STATEMENT
    print("Heads")
else:
    print("Tails")


#If you have more than two results, elif is good to check one, then another, then as many as you
#need, and if none of the conditions are met, else is a kinda-sorta "fallback".

a = random.randint(1,5)
b = random.randint(1,5)

print(a, b)

if a > b:
    print("A is greater than B")
elif a < b:
    print("A is less than B")
elif a == b:
    print("A is equal to B")


#Additonally, you can have one or more conditions on the same line using "and" and "or".

#or = One statement must be true, even if the other is false (both can also be true).
#and = Both conditions must be true.

c = 6
d = 6
e = 9

if c <= d and c <= e:
    print("C is the smallest number")
elif c > d or c > e:
    print("C is NOT the smallest number")


#You can use conditional statements to do one set of math or another based on specific conditions.
#This is a permanent change that will affect later code until it is changed back or the code is rerun.

f = 9
g = 3

if f < g:
    f = f + g
    print(f)
elif f >= g:
    f -= g
    print(f)


#This is an example use of modulo. In this example, if the modulo 2 of a number is zero,
#that means it's even because it's divisible by 2. You can change the modulo number to check
#for similar things (EX: x % 3 == 0 is divisible by 3, etc.)

h = random.randint(1,100)

if h % 2 == 0:
    print(f"{h} is even")
else:
    print(f"{h} is odd")


#This is a nested conditional statement. You can nest them inside of each other
#to create more complex pathways and conditions if you need to be more precise.

i = random.randint(1,30)

if i > 10:
    if i > 20:
        print(f"{i} is greater than 20!")
    else:
        print(f"{i} is greater than 10 but less than 20!")
elif i <= 10:
    if i > 5:
        print(f"{i} is greater than 5 but less than 10!")
    else:
        print(f"{i} is less than or equal to 5")
