#Name: Coach Mack
#Class: 6th Hour
#Assignment: Semester Project 1

import random
import time

#Due to weird time travelling circumstances beyond explanation, you find yourself in 2018 or so
#working for Larian Studios. Currently, they are working on the early prototypes of the hype
#upcoming game "Baldur's Gate 3". BG3 is a game that uses the Dungeons & Dragons 5th edition rules
#as its framework for gameplay. You have been given a basic dictionary of some of the main hero
#characters and some of the enemies they may face, and are tasked with making an early prototype
#of one of the party members fighting against an enemy until one of them hits zero HP (dies).

partyDict = {
    "LaeZel" : {
        "HP" : 48,
        "Init" : 1,
        "AC" : 17,
        "AtkMod": 6,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 3
    },
    "Shadowheart" : {
        "HP" : 40,
        "Init" : 1,
        "AC" : 18,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 3,
    },
    "Gale" : {
        "HP" : 32,
        "Init" : 1,
        "AC" : 14,
        "AtkMod": 6,
        "Damage" : random.randint(1,10) + random.randint(1,10),
    },
    "Astarion" : {
        "HP" : 40,
        "Init" : 3,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,8) + random.randint(1,6) + 4,
    }
}

enemyDict = {
    "Goblin" : {
        "HP" : 7,
        "Init" : 0,
        "AC" : 12,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 2
    },
    "Orc": {
        "HP" : 15,
        "Init": 1,
        "AC" : 13,
        "AtkMod": 5,
        "Damage" : random.randint(1,12) + 3
    },
    "Troll": {
        "HP" : 84,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 4
    },
    "Mindflayer": {
        "HP" : 71,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + 4
    },
    "Dragon": {
        "HP" : 127,
        "Init": 2,
        "AC" : 18,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4
    },
}

#Combat consists of these steps:

#1. Rolling for 'initiative' to see who goes first. This is determined by rolling a
#20-sided die (d20) and adding their initiative modifier (If the roll is the same,
#assume the hero goes first).
gale_init_roll = random.randint(1,20) + partyDict["Gale"]["Init"]
orc_init_roll = random.randint(1,20) + enemyDict["Orc"]["Init"]
if gale_init_roll >= orc_init_roll:
    print("Gale goes first!")
    hero_first = True
else:
    print("Orc goes first!")
    hero_first = False
#2. Rolling to attack. This is determined by rolling a 20-sided die (d20) and adding their
#attack modifier. The attack hits if it matches or is higher than the target's Armor Class (AC).
#If the d20 rolled to attack is an unmodified ("natural") 20, the attack automatically hits and
#the character deals double damage. If the d20 rolled to attack is an unmodified ("natural") 1,
#the attack automatically misses

#3. If the attack hits, roll damage and subtract it from the target's hit points.

#4. The second in initiative rolls to attack (and rolls damage) afterwards.

#5. Repeat steps 2-5 until one of the characters is dead.

if hero_first == True:
    while partyDict["Gale"]["HP"] > 0 or enemyDict["Orc"]["HP"] > 0:
        gale_atk_roll = random.randint(1, 20)
        if gale_atk_roll == 20:
            print("Critical Hit!")
            enemyDict["Orc"]["HP"] -= (partyDict["Gale"]["Damage"] * 2)
        elif gale_atk_roll == 1:
            print("Critial Miss!")
        elif gale_atk_roll + partyDict["Gale"]["AtkMod"] >= enemyDict["Orc"]["AC"]:
            print("Gale hits!")
            enemyDict["Orc"]["HP"] -= (partyDict["Gale"]["Damage"])
        elif gale_atk_roll + partyDict["Gale"]["AtkMod"] < enemyDict["Orc"]["AC"]:
            print("Gale misses!")

        if enemyDict["Orc"]["HP"] <= 0:
            print("The Orc is dead!")
            break
        else:
            print(f"Orc has {enemyDict["Orc"]["HP"]} HP")

        orc_atk_roll = random.randint(1, 20)
        if orc_atk_roll == 20:
            print("Critical Hit!")
            partyDict["Gale"]["HP"] -= (enemyDict["Orc"]["Damage"] * 2)
        elif orc_atk_roll == 1:
            print("Critial Miss!")
        elif orc_atk_roll + enemyDict["Orc"]["AtkMod"] >= partyDict["Gale"]["AC"]:
            print("Orc hits!")
            partyDict["Gale"]["HP"] -= (enemyDict["Orc"]["Damage"])
        elif orc_atk_roll + enemyDict["Orc"]["AtkMod"] < partyDict["Gale"]["AC"]:
            print("Orc misses!")

        if partyDict["Gale"]["HP"] <= 0:
            print("The Gale is dead!")
            break
        else:
            print(f"Gale has {partyDict["Gale"]["HP"]} HP.")

elif hero_first == False:
    while partyDict["Gale"]["HP"] > 0 or enemyDict["Orc"]["HP"] > 0:
        orc_atk_roll = random.randint(1, 20)
        if orc_atk_roll == 20:
            print("Critical Hit!")
            partyDict["Gale"]["HP"] -= (enemyDict["Orc"]["Damage"] * 2)
        elif orc_atk_roll == 1:
            print("Critial Miss!")
        elif orc_atk_roll + enemyDict["Orc"]["AtkMod"] >= partyDict["Gale"]["AC"]:
            print("Orc hits!")
            partyDict["Gale"]["HP"] -= (enemyDict["Orc"]["Damage"])
        elif orc_atk_roll + enemyDict["Orc"]["AtkMod"] < partyDict["Gale"]["AC"]:
            print("Orc misses!")

        if partyDict["Gale"]["HP"] <= 0:
            print("The Gale is dead!")
            break
        else:
            print(f"Gale has {partyDict["Gale"]["HP"]} HP.")

        gale_atk_roll = random.randint(1, 20)
        if gale_atk_roll == 20:
            print("Critical Hit!")
            enemyDict["Orc"]["HP"] -= (partyDict["Gale"]["Damage"] * 2)
        elif gale_atk_roll == 1:
            print("Critial Miss!")
        elif gale_atk_roll + partyDict["Gale"]["AtkMod"] >= enemyDict["Orc"]["AC"]:
            print("Gale hits!")
            enemyDict["Orc"]["HP"] -= (partyDict["Gale"]["Damage"])
        elif gale_atk_roll + partyDict["Gale"]["AtkMod"] < enemyDict["Orc"]["AC"]:
            print("Gale misses!")

        if enemyDict["Orc"]["HP"] <= 0:
            print("The Orc is dead!")
            break
        else:
            print(f"Orc has {enemyDict["Orc"]["HP"]} HP")

