# The player!

# External imports
import libtcodpy as libtcod

# Internal imports
from CreatureClass import *

class Player(Creature):
    
    def __init__(self, map):
        super(Player, self).__init__(symbol = '@', color = libtcod.white)
        
        self.fovMap = map
        # Set up FOV map
        