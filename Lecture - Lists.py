#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Lists


#This is a list. In essence, it's a variable that has multiple values inside that
#you can pull from any of them without needing to make multiple variables for each
#piece of data. This is useful for cases where you have a lot of the same type of
#"thing", such as names in this example.
robot_santas_list = ["Connor", "Devon", "Alaya", "Shane", "Eli", "Ally", "Tristan", "Carlos",
                     "Ethan", "GREG", "Kash", "Brodie"]

#To print the list. You simply name the variable followed by [] with the
#number inside being its "index" location.
#Note that all indexes START AT ZERO. Not one. :)
print(robot_santas_list)
print(robot_santas_list[6], "is NAUGHTY!")
print(f"{robot_santas_list[9]} is NAUGHTY!")

#This is the append function. This allows you to tack on a new value or "object"
#to the end of the list.
robot_santas_list.append("Aaden")
print(robot_santas_list)

#This is the remove function. It removes every instance of the value.
robot_santas_list.remove("Aaden")
print(robot_santas_list)

#This is the insert function. It works like the append function but
#you can place the object anywhere inside of the list, not just at the end.
robot_santas_list.insert(3, "Aaden")
print(robot_santas_list)


#This is a number list. You can place any kind of object in a list,
#not just strings.
num_list = [7, 6, 57, 22, 6398, 1, 13, 24, 670, 1300254, 7, 1000, 158000000]
print(num_list)

#You can sort the list from lowest to highest. When you sort a list,
#it permanently changes the order of the list so keep that in mind.
num_list.sort()
print(num_list)

#You can also sort the list from highest to lowest using the
#reverse=True modifier.
num_list.sort(reverse=True)
print(num_list)

#You can do math with the numbers in a list. Simply call their
#index location. Reminder: START AT ZERO.
print(num_list[1] + num_list[0] + num_list[5])

#If you need to add them all together, there is a sum function
#that lets you add the contents of a list together.
print(sum(num_list))


#You can also list different types of objects in the same list.
mix_list = ["Todd", 2, False]
print(mix_list)

#You can also put an input() function inside of an index location
#call to print out whichever part of the list you want.
print(mix_list[int(input())])