class Character:
    def __init__(self, name: str) -> None:
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

        print(f"{self.name} Attacked {opponent.name}\n1. Health Impact - {h_impact} || Remaining - {opponent.health}\n2. Strength Impact - {s_impact} || Remaining - {opponent.strength}\n\n")

        if not opponent.isAlive():
            return print(f"{self.name} has won!")
            


class ApeMan(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.type = "Ape Man"
        self.health: float = 150.0
        self.strength: float = 200.0

class Hercules(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.type = "Hercules"
        self.health: float = 200.0
        self.strength: float = 200.0

class Assassin(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.type = "Assassin"
        self.health: float = 250.0
        self.strength: float = 100.0