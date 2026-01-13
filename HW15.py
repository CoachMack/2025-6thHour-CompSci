#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter Value for A:"))
b = int(input("Enter Value for B:"))
c = int(input("Enter Value for C:"))
#4. Add a and b together, then divide the sum by c. Print the result.
result = (a + b) / c
print(result)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
result_rounded = round(result)
print(result_rounded)
if result_rounded % 2 == 0:
    print("It is even")
else:
    print("It is odd")
#6. Create a list of five different random integers between 1 and 10.
rand_int_list = [random.randint(1,10),
                 random.randint(1,10),
                 random.randint(1,10),
                 random.randint(1,10),
                 random.randint(1,10)]
#7. Print the 4th number in the list.
print(rand_int_list)
print(rand_int_list[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
rand_int_list.append(random.randint(1,10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
rand_int_list.sort()
print(rand_int_list)
print(rand_int_list[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i <= 100:
    print(i)
    i += i
#11. Create a list containing the names of five other students in the classroom.
student_list = ["Alaya", "Ally", "Greg", "Carlos", "Connor", "Devon"]
#12. Create a for loop that individually prints out the names of each student in the list.
for j in student_list:
    print(j)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for k in range(1,101):
    print(k)
    if k % 10 == 0:
        break
#14. Free space. Do something creative. :)
print("From the moment I understood the weakness of my flesh, it disgusted me. "
      "I craved the strength and certainty of steel. I aspired to the purity of the "
      "Blessed Machine. Your kind cling to your flesh, as though it will not decay "
      "and fail you. One day the crude biomass you call a temple will wither, and "
      "you will beg my kind to save you. But I am already saved, for the Machine is "
      "immortal… Even in death I serve the Omnissiah.")