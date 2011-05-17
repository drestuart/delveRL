# External imports
import libtcodpy as libtcod

# Internal imports
from AlignmentClass import *
from AIClass import *
from GetSetClass import *

class Creature(GetSet):
    #combat-related properties and methods (monster, player, NPC).
    def __init__(self, name, hp, map, x = -1, y = -1, stats = (10, 10, 10), alignment = Alignment("N"),
    maxEnergy = 100, moveCost = 100, attackCost = 100, ai = None,
    inventory = None, deathFunction=None, baseSymbol = "@", baseColor = libtcod.red,
    baseBackground = libtcod.BKGND_NONE):
        self.deathFunction = deathFunction
        self.max_hp = hp
        self.hp = hp
        self.name = name
        
        if ai == None:
            ai = NormalMonsterAI()
        self.ai = ai
        self.ai.setOwner(self)
        
        self.baseSymbol = baseSymbol
        self.baseColor = baseColor
        self.baseBackground = baseBackground
        
        self.visible = True
        
        self.energy = maxEnergy
        self.maxEnergy = maxEnergy
        self.moveCost = moveCost
        self.attackCost = attackCost
        
        self.map = map
        self.x = x
        self.y = y
        
    def move(self, dx, dy):
               
        if self.map.tiles[self.x + dx][self.y + dy].addCreature(self):
            
            #Remove self from the old tile
            self.map.tiles[self.x][self.y].creature = None
        
            self.x += dx
            self.y += dy
            #self.energy -= self.moveCost
                        
            print self.name + " moves to", self.x, self.y
            return True
        
        else:
            return False

    def heal(self, amount):
        #heal by the given amount, without going over the maximum
        self.hp = min(self.hp + amount, self.max_hp)

    def takeDamage(self, damage):
        #apply damage if possible
        if damage > 0:
            self.hp -= damage
            #check for death. if there's a death function, call it
            if self.hp <= 0:
                function = self.deathFunction
                if function is not None:
                    function(self.owner)

    def passTime(self, turns = 1):
        print "It is " + self.name + "'s turn"
        for i in range(turns):
            self.takeTurn() 

    def takeTurn(self):
        self.ai.takeTurn()
    
    def isVisible(self):
        return self.visible
    
    def color(self):
        # There will probably be some more logic here
        return self.baseColor
    
    def symbol(self):
        return self.baseSymbol
    
    def background(self):
        return self.baseBackground

#    def attack(self, target):
#        #a simple formula for attack damage
#        damage = self.power - target.fighter.defense
# 
#        if damage > 0:
#            #make the target take some damage
#            message(self.owner.name.capitalize() + ' attacks ' + target.name + ' for ' + str(damage) + ' hit points.')
#            target.fighter.take_damage(damage)
#        else:
#            message(self.owner.name.capitalize() + ' attacks ' + target.name + ' but it has no effect!')

def randomCreature(map):
    return Creature('orc', 10, map, baseSymbol = 'o')

def main():
    Creature(10)

if __name__ == '__main__':
    main()






