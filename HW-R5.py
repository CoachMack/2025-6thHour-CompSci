#Name: Coach
#Class: 6th Hour
#Assignment: HW-R5

#1. Fix the "class" comment at the top to "6th Hour"
print("Here you go, Ally :)")
#2. Create a list of the names of all the students in the classroom.
stu_list = ["Alaya", "Tristan", "Devon", "Ally", "GREGG", "Shane", "Ethan", "Connor"]
#3. Create a for loop that prints the names of every student in the list.
#for i in stu_list:
    #print(i)
#4. Using the "in" operator (hint: Google), create a for loop that only prints
#the name of a student if the letter "e" is in it.
for j in stu_list:
    if "e" in j or "E" in j:
        print(j)