#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Dictionaries


#This is a dictionary. It works a lot like a "list of lists" in that you can nest dictionaries
#inside of other dictionaries. What makes it different from lists is that it uses "keys" instead
#of index numbers. The keys are labels that you tie to a value.
kashCarDict = {
    "brand" : "Chevrolet",
    "model" : "Silverado",
    "year" : [2004, 2025]
}

#If you want to print the whole dictionary, print the name of the dictionary like you would a variable.
print(kashCarDict)

#If you want to print a specific value, put the key inside of a box like you would pulling from a list.
print(kashCarDict["brand"])

#If the value itself is a list, you put another box and call the index location like so.
print(kashCarDict["year"][1])

#You can print just the keys from a dictionary using the keys function.
print(kashCarDict.keys())

#You can print just the values from a dictionary using the values function.
print(kashCarDict.values())


#You can put dictionaries inside dictionaries. This is called a nested dictionary.
#By doing this, you can organize values in a more robust way. Remember, you need to put the key
#names inside of quotes like a string, even if it's anotheer dictionary
sixth_hour_class = {
    "student_1" : {
        "Name" : "Ally",
        "Grade" : 12,
        "Sports" : False,
    },
    "student_2" : {
        "Name" : "Aaden",
        "Grade" : 11,
        "Sports" : True,
    },
    "student_3" : {
        "Name" : "Ethan",
        "Grade" : 9,
        "Sports" : True,
    },
}

#If you want to call the value of a key within a nested dictionary, use two boxes:
#1 with the name of the nested dictionary, 1 with the name of the key within the nested dictionary.
print(sixth_hour_class["student_1"]["Grade"])
print(sixth_hour_class["student_2"]["Sports"])

#If you want to force change a key's value, just call the key and then have it equal the new value.
#However, this is a dirty way to do it that might cause issues.
sixth_hour_class["student_1"]["Sports"] = True
print(sixth_hour_class["student_1"]["Sports"])

#A cleaner way to do it is with the update function. Additionally, update allows you to add a new key
#and value to the dictionary.
sixth_hour_class["student_2"].update({"Last Name" : "Hampton"})
print(sixth_hour_class["student_2"])

#The pop function removes keys (and the values tied to it) for dictionaries as well.
sixth_hour_class["student_2"].pop("Last Name")
print(sixth_hour_class["student_2"])

