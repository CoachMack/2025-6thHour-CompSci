#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW6


#1. Import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three different variables that each randomly generate an integer between 1 and 10
r1 = random.randint(1,10)
r2 = random.randint(1,10)
r3 = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(r1, r2, r3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
r1 = r1 + 2
r2 -= 4
r3 *= 1.5
#6. Print each result from #5 on the same line.
print(r1, r2, r3)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
randint_list = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
randint_list.sort()
print(randint_list)
#9. Add together the highest three numbers in the list from #7 and print the result.
print(randint_list[1] + randint_list[2] + randint_list[3])
#10. Create a list with 5 names of other students in this class and print the list.
name_list = ["Dave", "Jude", "Hogan", "Aiden", "Ashton"]
print(name_list)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(name_list)
print(name_list)
#12. Print a random choice from the list of names from #10.
print(random.choice(name_list))
