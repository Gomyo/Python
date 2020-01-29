class Wizard:
    def stats(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print('파이어볼')

x = Wizard() #Create instance using 'Class'

Wizard.stats(x, health=545, mana=210, armor=10) #Making x's stats
print(x.health, x.mana, x.armor)
x.attack()