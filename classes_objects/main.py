#Max Holdaway Classes and Objects notes

#What is a class?
class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nHp: {self.hp}\nDmg: {self.dmg}"

    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f"{self.name} attacked {opponent.name} for {self.dmg} and {opponent.name} has {opponent.hp}")
            if opponent.hp > 0:
                self.hp -= opponent.dmg
                print(f"{opponent.name} attacked {self.name} for {opponent.dmg} and {self.name} has {self.hp}")
                if self.hp <= 0:
                    print(f"{self.name} has fainted. {opponent.name} has won.")
                    self.hp = 0
            else:
                print(f"{opponent.name} has fainted. {self.name} has won.")
                opponent.hp = 0

bob = pokemon("Mr.Bob", "Charizard", 300, 95)
fluffy = pokemon("Fluffy", "Arcanine", 280, 110)
print(bob)
print(fluffy)

bob.battle(fluffy)