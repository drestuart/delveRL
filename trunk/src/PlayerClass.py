# The player!

# External imports
import libtcodpy as libtcod

# Internal imports
from CreatureClass import *
from AIClass import *

class Player(Creature):
    
    def __init__(self, map):
        super(Player, self).__init__('player', 10, map, base_symbol = '@', base_color = libtcod.white, ai = PlayerAI())
        
        self.fovMap = map
        # Set up FOV map
        
        
            