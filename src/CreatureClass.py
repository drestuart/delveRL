# External imports
import libtcodpy as libtcod

# Internal imports
from AlignmentClass import *
from AIClass import *

class Creature:
    #combat-related properties and methods (monster, player, NPC).
    def __init__(self, hp, stats = (10, 10, 10), alignment = Alignment("N"),
    energy = 100, move_cost = 100, attack_cost = 100, ai = NormalMonster(),
    inventory = None, death_function=None, base_symbol = "@", base_color = libtcod.red,
    base_background = libtcod.BKGND_NONE):
        self.death_function = death_function
        self.max_hp = hp
        self.hp = hp
        self.base_symbol = base_symbol
        self.base_color = base_color
        self.base_background = base_background
        self.visible = True
        

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

    def passTime(self, turns = 1):
        for i in range(turns):
            self.takeTurn() 

    def takeTurn(self):
        pass
    
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

def randomCreature():
    return Creature(10, base_symbol = 'o')

def main():
    Creature(10)

if __name__ == '__main__':
    main()






