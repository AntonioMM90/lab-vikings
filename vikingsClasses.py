import random
# Soldier


class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        self.power = self.strength
        return self.power

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
    
    pass

# Viking


class Viking(Soldier):
    def __init__ (self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return (f"{self.name} has received {damage} points of damage")
        else:
            return (f"{self.name} has died in act of combat")
    def battleCry(self):
        return "Odin Owns You All!"
    pass

# Saxon

class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return (f"A Saxon has died in combat")

    pass

# War


class War:
    def __init__ (self):
        self.saxonArmy = []
        self.vikingArmy = []

    def addViking(self, Viking):
        self.Viking = Viking
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.Saxon = Saxon
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        s = random.choice(self.saxonArmy)
        v = random.choice(self.vikingArmy)
        if s.health <=0:
            self.saxonArmy.remove(s)
        return s.receiveDamage(v.strength)
    
    def saxonAttack(self):
        s = random.choice(self.saxonArmy)
        v = random.choice(self.vikingArmy)
        if v.health <=0:
            self.vikingArmy.remove(v)
        return v.receiveDamage(s.strength)

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    pass
