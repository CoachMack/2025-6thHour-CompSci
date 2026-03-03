#Name: Coach Mack
#Class: 6th Hour
#Assignment: Scenario 6


#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Semester Project 1 using classes instead of dictionaries, include and refactor
#the combat test code below as well.)

import random
import time

class Creature:
    def __init__(self, name, HP, init, AC, ATK, DMG):
        self.name = name
        self.HP = HP
        self.init = init
        self.AC = AC
        self.ATK = ATK
        self.DMG = DMG

    def laezel_dmg_roll(self):
        laezel_dmg = random.randint(1,6) + random.randint(1,6) + 3
        self.DMG = laezel_dmg

    def sheart_dmg_roll(self):
        sheart_dmg = random.randint(1,6) + 3
        self.DMG = sheart_dmg

    def gale_dmg_roll(self):
        gale_dmg = random.randint(1,10) + random.randint(1,10)
        self.DMG = gale_dmg

    def astarion_dmg_roll(self):
        astarion_dmg = random.randint(1,8) + random.randint(1,6) + 4
        self.DMG = astarion_dmg

    def goblin_dmg_roll(self):
        goblin_dmg = random.randint(1,6) + 2
        self.DMG = goblin_dmg

    def orc_dmg_roll(self):
        orc_dmg = random.randint(1,12) + 3
        self.DMG = orc_dmg

    def troll_dmg_roll(self):
        troll_dmg = random.randint(1,6) + random.randint(1,6) + 4
        self.DMG = troll_dmg

    def mindflayer_dmg_roll(self):
        mindflayer_dmg = random.randint(1,10) + random.randint(1,10) + 4
        self.DMG = mindflayer_dmg

    def dragon_dmg_roll(self):
        dragon_dmg = random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4
        self.DMG = dragon_dmg



LaeZel = Creature("Lae'zel", 48,1,17,6,0)
Shadowheart = Creature("Shadowheart", 40, 1, 18, 4,0)
Gale = Creature("Gale", 32, 1, 14, 6,0)
Astarion = Creature("Astarion", 40,3,14,5,0)

Goblin = Creature("Goblin", 7, 0, 12, 4, 0)
Orc = Creature("Orc", 15, 1, 13, 5, 0)
Troll = Creature("Troll",84, 1, 15, 7, 0)
Mindflayer = Creature("Mindflayer", 71, 1, 15, 7, 0)
Dragon = Creature("Dragon", 127, 2, 18, 7, 0)

#Combat Code
def hero_attack():
    while Gale.HP > 0 or Orc.HP > 0:
        print(f"{Gale.name} attacks!")
        time.sleep(1)
        gale_atk_roll = random.randint(1, 20)
        if gale_atk_roll == 20:
            Gale.gale_dmg_roll()
            print(f"Critical Hit! {Gale.name} does {Gale.DMG * 2} damage!")
            Orc.HP -= (Gale.DMG * 2)
        elif gale_atk_roll == 1:
            print("Critial Miss!")
        elif gale_atk_roll + Gale.ATK >= Orc.AC:
            Gale.gale_dmg_roll()
            print(f"{Gale.name} hits and does {Gale.DMG} damage!")
            Orc.HP -= (Gale.DMG)
        elif gale_atk_roll + Gale.ATK < Orc.AC:
            print(f"{Gale.name} misses!")
        time.sleep(1)

        if Orc.HP <= 0:
            print(f"The {Orc.name} is dead!")
            exit()
        else:
            print(f"{Orc.name} has {Orc.HP} HP")
            enemy_attack()

def enemy_attack():
    while Gale.HP > 0 or Orc.HP > 0:
        print(f"{Orc.name} attacks!")
        time.sleep(1)
        orc_atk_roll = random.randint(1, 20)
        if orc_atk_roll == 20:
            Orc.orc_dmg_roll()
            print(f"Critical Hit! The Orc does {Orc.DMG * 2} damage!")
            Gale.HP -= (Orc.DMG * 2)
        elif orc_atk_roll == 1:
            print("Critial Miss!")
        elif orc_atk_roll + Orc.ATK >= Gale.AC:
            Orc.orc_dmg_roll()
            print(f"{Orc.name} hits and does {Orc.DMG} damage!")
            Gale.HP -= (Orc.DMG)
        elif orc_atk_roll + Orc.ATK < Gale.AC:
            print(f"{Orc.name} misses!")
        time.sleep(1)

        if Gale.HP <= 0:
            print(f"{Gale.name} is dead!")
            exit()
        else:
            print(f"{Gale.name} has {Gale.HP} HP.")
            hero_attack()

def initiative_roll():
    gale_init_roll = random.randint(1,20) + Gale.init
    orc_init_roll = random.randint(1,20) + Orc.init
    print("Combat Encounter!")
    time.sleep(1)
    print(f"Gale rolled {gale_init_roll}, Orc rolled {orc_init_roll}")
    time.sleep(1)
    if gale_init_roll >= orc_init_roll:
        print("Gale goes first!")
        time.sleep(1)
        hero_attack()
    else:
        print("Orc goes first!")
        time.sleep(1)
        enemy_attack()

initiative_roll()