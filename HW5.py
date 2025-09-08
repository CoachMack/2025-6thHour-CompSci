#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
num_list = [0,1,2,3,4,5,6,7,8]
#2. Sort the list from highest to lowest.
num_list.sort(reverse=True)
#3. Create an empty list.
emp_list = []
#4. Remove the median number from the first list and add it to the second list.
placeholder = num_list[4]
num_list.pop(4)
emp_list.append(placeholder)

#5. Remove the first number from the first list and add it to the second list.
emp_list.append(num_list.pop(0))
#6. Print both lists.
print(num_list)
print(emp_list)
#7. Add the two numbers in the second list together and print the result.
emp_list_sum = sum(emp_list)
print(emp_list_sum)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
num_list.append(emp_list_sum)
emp_list.pop(0)
emp_list.pop(0)
#9. Sort the first list from lowest to highest and print it.
num_list.sort()
print(num_list)