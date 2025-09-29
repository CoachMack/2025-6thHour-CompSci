#Name: Coach Mack
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.


enemy_dict = {
    "enemy1" : {
        "Name" : "Goblin",
        "HP" : 6,
        "DMG" : 2,
        "AC" : 12
    },
    "enemy2" : {
        "Name" : "Orc",
        "HP" : 14,
        "DMG" : 6,
        "AC" : 14
    },
    "enemy3" : {
        "Name" : "Troll",
        "HP" : 22,
        "DMG" : 10,
        "AC" : 13
    },
    "enemy4" : {
        "Name" : "Bugbear",
        "HP" : 36,
        "DMG" : 18,
        "AC" : 16
    },
    "enemy5" : {
        "Name" : "Dragon",
        "HP" : 110,
        "DMG" : 44,
        "AC" : 17
    },
}

enemy_dict["enemy1"]["DMG"] = int(input("Change Goblin Damage: "))
print(enemy_dict["enemy1"])

enemy_dict["enemy2"]["DMG"] = int(input("Change Orc Damage: "))
print(enemy_dict["enemy2"])

enemy_dict["enemy3"]["DMG"] = int(input("Change Troll Damage: "))
print(enemy_dict["enemy3"])

enemy_dict["enemy4"]["DMG"] = int(input("Change Bugbear Damage: "))
print(enemy_dict["enemy4"])

enemy_dict["enemy5"]["DMG"] = int(input("Change Dragon Damage: "))
print(enemy_dict["enemy5"])
