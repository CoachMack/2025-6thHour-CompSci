#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello World!")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
greg_dict = {
    "Name" : "Green Rupee of Eternal Glory",
    "Value" : [1, 5, 10],
    "Location" : "Castle Town",
}
#3. Print the keys of the dictionary from #2.
print(greg_dict.keys())
#4. Print the values of the dictionary from #2
print(greg_dict.values())
#5. Print one of the three numbers from the list by itself
print(greg_dict["Value"][0])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
greg_dict.update({"Obtained" : True})
#7. Print the entire dictionary from #2 with the updated key and value.
print(greg_dict)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
sixth_hour_class = {
    "student_1" : {
        "Name" : "Devon",
        "Candy" : "Kit-Kat",
        "Color" : "Blue",
    },
    "student_2" : {
        "Name" : "Kash",
        "Candy" : "Sour Patch Kids",
        "Color" : "Green",
    },
    "student_3" : {
        "Name" : "Alaya",
        "Candy" : "Kit-Kat",
        "Color" : "Purple",
    },
}
#9. Print the names of all three classmates on the same line.
print(sixth_hour_class["student_1"]["Name"],sixth_hour_class["student_2"]["Name"],sixth_hour_class["student_3"]["Name"],)
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
sixth_hour_class.pop("student_1")
print(sixth_hour_class)