# The player!

# External imports
import libtcodpy as libtcod

# Internal imports
from CreatureClass import *
from AIClass import *

class Player(Creature):
    
    def __init__(self, map):
        super(Player, self).__init__('player', 10, map, baseSymbol = '@', baseColor = libtcod.white, ai = PlayerAI())
        
        self.__dict__['fovMap'] = map
        # Set up FOV map
        
        
            