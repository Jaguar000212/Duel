from characters import *
import random
import time

def start():
    print("WELCOME TO 2V2 DUEL")
    print("Availabe Characters - Ape Man, Hercules, Assassin")
    p1_name = input("Enter Player 1 name : ")
    p1_character = input(f"Select {p1_name}'s character : ")
    p1 : Character = None

    if p1_character.lower() == "ape man":
        p1 = ApeMan(p1_name)
    elif p1_character.lower() == "hercules":
        p1 = Hercules(p1_name)
    elif p1_character.lower() == "assassin":
        p1 = Assassin(p1_name)
    else:
        print("Received invalid character. Selecting a random.")
        p1 = random.choice([ApeMan(p1_name), Hercules(p1_name), Assassin(p1_name)])

    print(f"\n{p1.name} selected {p1.type}!\n")
    

    p2_name = input("Enter Player 2 name : ")
    p2_character = input(f"Select {p2_name}'s character : ")
    p2 : Character = None

    if p2_character.lower() == "ape man":
        p2 = ApeMan(p2_name)
    elif p2_character.lower() == "hercules":
        p2 = Hercules(p2_name)
    elif p2_character.lower() == "assassin":
        p2 = Assassin(p2_name)
    else:
        print("Received invalid character. Selecting a random.")
        p2 = random.choice([ApeMan(p2_name), Hercules(p2_name), Assassin(p2_name)])

    print(f"\n{p2.name} selected {p2.type}!\n")


    while True:
        p1.attack(p2)
        if not p2.isAlive():
            break
        else:
            time.sleep(2)
            p2.attack(p1)
            if p1.isAlive():
                time.sleep(2)
                continue
            else:
                break

start()