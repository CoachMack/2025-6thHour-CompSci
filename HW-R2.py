#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW-R2


#1. Print "Hello World!"
print("Hello World!")
#2. Create an empty list.
emp_list = []
#3. Create a list that contains the names of everyone in the classroom.
stu_list = ["Alaya", "Tristan", "Devon", "Ally", "GREGG", "Shane", "Ethan", "Connor"]
#4. Print the list from #3, sort the list, then print the list again.
print(stu_list)
stu_list.sort()
print(stu_list)
#5. Append 5 different integers into the empty list from #2 and print the list.
emp_list.append(1)
emp_list.append(2)
emp_list.append(3)
emp_list.append(4)
emp_list.append(7)
print(emp_list)
#6. Add together the middle three numbers in the list from #2 and print the result.
print(emp_list[1] + emp_list[2] + emp_list[3])
#7. Remove the very first number in the list from #2. Print the new first number.
emp_list.remove(emp_list[0])
print(emp_list[0])
#8. Create a dictionary with three keys with respective values: your name, your grade, and your favorite color.
CoachMack_Dict = {
    "Name" : "Coach Mack",
    "Grade" : "Teacher",
    "Color" : "Cyan"
}
#9. Using the update function, add a fourth key and value determining your favorite candy.
CoachMack_Dict.update({"Candy":"Toblerone"})
#10. Print ONLY the values of the dictionary from #8.
print(CoachMack_Dict.values())