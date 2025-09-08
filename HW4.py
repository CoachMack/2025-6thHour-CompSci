#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW4


#1. Print Hello World!
print("Hello World!")
#1. Create a list with 5 strings containing 5 different names in it.
name_list = ["Shane", "Greg", "Aaden", "Devon", "Alaya"]
#2. Append a new name onto the Name List.
name_list.append("Ethan")
#3. Print out the 4th name on the list.
print(name_list[3])
#4. Create a list with 4 different integers in it.
num_list = [375, 4, 68, 32]
#5. Insert a new integer into the 2nd spot and print the new list.
num_list.insert(1, 6472)
print(num_list)
#6. Sort the list from lowest to highest and print the sorted list.
num_list.sort()
print(num_list)
#7. Add the 1st three numbers on the sorted list together and print the sum.
first_three_sum = num_list[0] + num_list[1] + num_list[2]
print(first_three_sum)
#8. Create a list with two strings, two variables, and too boolean values.
mixed_up_list = ["John", "Pork", 6, 7, True, False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(mixed_up_list[int(input("Choose between 0 - 5: "))])
