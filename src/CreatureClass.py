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
        self.__dict__['deathFunction'] = deathFunction
        self.__dict__['max_hp'] = hp
        self.__dict__['hp'] = hp
        self.__dict__['name'] = name
        
        if ai == None:
            ai = NormalMonsterAI()
        self.__dict__['ai'] = ai
        self.ai.setOwner(self)
        
        self.__dict__['baseSymbol'] = baseSymbol
        self.__dict__['baseColor'] = baseColor
        self.__dict__['baseBackground'] = baseBackground
        
        self.__dict__['visible'] = True
        
        self.__dict__['energy'] = maxEnergy
        self.__dict__['maxEnergy'] = maxEnergy
        self.__dict__['moveCost'] = moveCost
        self.__dict__['attackCost'] = attackCost
        
        self.__dict__['map'] = map
        self.__dict__['x'] = x
        self.__dict__['y'] = y
        
    def move(self, dx, dy):
               
        if self.map.tiles[self.x + dx][self.y + dy].addCreature(self):
            
            #Remove self from the old tile
            self.map.tiles[self.x][self.y].removeCreature()
        
            self.setPosition(self.map, self.x + dx, self.y + dy)
            #self.energy -= self.moveCost
                        
            print self.name + " moves to", self.x, self.y
            return True
        
        else:
            return False
        
    def setPosition(self, map, x, y):
        self.__dict__['x'] = x
        self.__dict__['y'] = y
        self.__dict__['map'] = map
    
    def changeHP(self, amount):
        self.__dict__['hp'] = min(self.hp + amount, self.max_hp)
        if self.hp <= 0:
            self.deathFunction(self)

    def heal(self, amount):
        #heal by the given amount
        self.changeHP(amount)

    def takeDamage(self, damage):
        #apply damage if possible
        if damage > 0:
            self.changeHP(-damage)
            
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






