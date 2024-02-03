import random
import time
from tkinter import *


class Character:
    def __init__(self, name: str, window : Tk) -> None:
        self.name = name
        self.health: float = 100.0
        self.strength: float = 100.0

    def isAlive(self) -> bool:
        if self.health > 0 and self.strength > 0:
            return True
        return False

    def hit(self, h_impact: float, s_impact: float):
        self.health -= h_impact
        self.strength -= s_impact

    def attack(self, opponent):
        h_impact = (self.strength) / 4
        s_impact = 20

        if h_impact > opponent.health:
            h_impact = opponent.health

        if s_impact > opponent.strength:
            s_impact = opponent.strength

        opponent.hit(h_impact, s_impact)

        Label(root, text=f"{self.name} Attacked {opponent.name}\n1. Health Impact - {h_impact} || Remaining - {opponent.health}\n2. Strength Impact - {s_impact} || Remaining - {opponent.strength}\n\n").pack()

        if not opponent.isAlive():
            return Label(root, text=f"{self.name} has won!").pack()
            


class ApeMan(Character):
    def __init__(self, name: str, window : Tk) -> None:
        super().__init__(name, window)
        self.type = "Ape Man"
        self.health: float = 150.0
        self.strength: float = 200.0

class Hercules(Character):
    def __init__(self, name: str, window : Tk) -> None:
        super().__init__(name, window)
        self.type = "Hercules"
        self.health: float = 200.0
        self.strength: float = 200.0

class Assassin(Character):
    def __init__(self, name: str, window : Tk) -> None:
        super().__init__(name, window)
        self.type = "Assassin"
        self.health: float = 250.0
        self.strength: float = 100.0

root = Tk()
p1_name = StringVar()
p1_character = StringVar()

p2_name = StringVar()
p2_character = StringVar()

def start():

    if p1_character.get().lower() == "ape man":
        p1 = ApeMan(p1_name.get(), root)
    elif p1_character.get().lower() == "hercules":
        p1 = Hercules(p1_name.get(), root)
    elif p1_character.get().lower() == "assassin":
        p1 = Assassin(p1_name.get(), root)
    else:
        Label(root, text="Received invalid character. Selecting a random.")
        p1 = random.choice([ApeMan(p1_name.get(), root), Hercules(p1_name.get(), root), Assassin(p1_name.get(), root)])

    Label(root, text=f"\n{p1.name} selected {p1.type}!\n").pack()


    if p2_character.get().lower() == "ape man":
        p2 = ApeMan(p2_name.get(), root)
    elif p2_character.get().lower() == "hercules":
        p2 = Hercules(p2_name.get(), root)
    elif p2_character.get().lower() == "assassin":
        p2 = Assassin(p2_name.get(), root)
    else:
        Label(root, text="Received invalid character. Selecting a random.").pack()
        p2 = random.choice([ApeMan(p2_name.get(), root), Hercules(p2_name.get(), root), Assassin(p2_name.get(), root)])

    Label(root, text=f"\n{p2.name} selected {p2.type}!\n").pack()


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

Label(root, text="WELCOME TO 2V2 DUEL").pack()
Label(root, text="Availabe Characters - Ape Man, Hercules, Assassin").pack()
Label(root, text="Player 1 Name").pack()
Entry(root, textvariable=p1_name).pack()
Label(root, text="Player 1 Character").pack()
Entry(root, textvariable=p1_character).pack()
p1 : Character = None

Label(root, text="Player 2 Name").pack()
Entry(root, textvariable=p2_name).pack()
Label(root, text="Player 2 Character").pack()
Entry(root, textvariable=p2_character).pack()
p1 : Character = None

Button(root, text="Start", command=start).pack()

root.mainloop()