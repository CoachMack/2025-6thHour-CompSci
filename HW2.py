#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW2


#1. Print "Hello World!"
print("Hello World!")
#2. Create three different variables with distinct names and values: one with an integer, one with a string, one with a boolean.
student_name = "Alaya"
student_grade = 9
student_sports = True
#3. Print all three variables on the same print function (at the same time).
print(student_name, student_grade, student_sports)
#4. Create a variable that asks the user to input an integer.
grade_skip_prompt = int(input("Enter Grades Skipped "))
#5. Add the integer variable from #2 with the integer from #4 and print the result.
student_new_grade = grade_skip_prompt + student_grade
print(student_new_grade)
#6. Take the result from #5 and divide it by 2. Print the result.
print(student_new_grade / 2)
#7. Change the value of the boolean variable to the opposite value (if true then make false, or vice versa).
student_sports = False
#8. Print the value of the boolean variable.
print(student_sports)
#9. Create a variable with a number that contains decimals.
student_gpa = 3.14
#10. Round the number from #9 up or down using the round function.
student_rounded_gpa = round(student_gpa)
print(student_rounded_gpa)

print(round(student_gpa))