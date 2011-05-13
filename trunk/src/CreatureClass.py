# External imports
import libtcodpy as libtcod

# Internal imports
from AlignmentClass import *
from AIClass import *

class Creature(object):
    #combat-related properties and methods (monster, player, NPC).
    def __init__(self, name, hp, map, x = -1, y = -1, stats = (10, 10, 10), alignment = Alignment("N"),
    max_energy = 100, move_cost = 100, attack_cost = 100, ai = NormalMonster(),
    inventory = None, death_function=None, base_symbol = "@", base_color = libtcod.red,
    base_background = libtcod.BKGND_NONE):
        self.death_function = death_function
        self.max_hp = hp
        self.hp = hp
        self.name = name
        
        self.base_symbol = base_symbol
        self.base_color = base_color
        self.base_background = base_background
        
        self.visible = True
        
        self.energy = max_energy
        self.max_energy = max_energy
        self.move_cost = move_cost
        self.attack_cost = attack_cost
        
        self.map = map
        self.x = x
        self.y = y
        
    def move(self, dx, dy):
               
        if self.map.tiles[self.x + dx][self.y + dy].add_creature(self):
            
        
            self.x += dx
            self.y += dy
            #self.energy -= self.move_cost
            
            #Remove self from the old tile
            self.map.tiles[self.x - dx][self.y - dy].creature = None
            
            
            print "Moving " + self.name + " to ", self.x, self.y
            return True
        
        else:
            return False

    def heal(self, amount):
        #heal by the given amount, without going over the maximum
        self.hp = min(self.hp + amount, self.max_hp)

    def take_damage(self, damage):
        #apply damage if possible
        if damage > 0:
            self.hp -= damage
            #check for death. if there's a death function, call it
            if self.hp <= 0:
                function = self.death_function
                if function is not None:
                    function(self.owner)

    def pass_time(self, turns = 1):
        print "It is " + self.name + "'s turn"
        for i in range(turns):
            self.take_turn() 

    def take_turn(self):
        print self.name, "takes its turn"
    
    def is_visible(self):
        return self.visible
    
    def color(self):
        # There will probably be some more logic here
        return self.base_color
    
    def symbol(self):
        return self.base_symbol
    
    def background(self):
        return self.base_background

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
    return Creature('orc', 10, map, base_symbol = 'o')

def main():
    Creature(10)

if __name__ == '__main__':
    main()






