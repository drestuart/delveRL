# The player!

# External imports
import libtcodpy as libtcod

# Internal imports
from CreatureClass import *

class Player(Creature):
    
    def __init__(self, map):
        super(Player, self).__init__('player', 10, map, base_symbol = '@', base_color = libtcod.white)
        
        self.fovMap = map
        # Set up FOV map
        
        
    def take_turn(self):
        print "Waiting for player"
        key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED)

        if key.vk == libtcod.KEY_ENTER and libtcod.KEY_ALT:
            #Alt+Enter: toggle fullscreen
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
        elif key.vk == libtcod.KEY_ESCAPE:
            exit(0)  #exit game
 
        elif key.vk == libtcod.KEY_UP or key.vk == libtcod.KEY_KP8:
            self.move(0, -1)
 
        elif key.vk == libtcod.KEY_DOWN or key.vk == libtcod.KEY_KP2:
            self.move(0, 1)
 
        elif key.vk == libtcod.KEY_LEFT or key.vk == libtcod.KEY_KP4:
             self.move(-1, 0)
 
        elif key.vk == libtcod.KEY_RIGHT or key.vk == libtcod.KEY_KP6:
            self.move(1, 0)

        elif key.vk == libtcod.KEY_KP1:
            self.move(-1, 1)

        elif key.vk == libtcod.KEY_KP3:
            self.move(1, 1)
            
        elif key.vk == libtcod.KEY_KP7:
            self.move(-1, -1)
        
        elif key.vk == libtcod.KEY_KP9:
            self.move(1, -1)
        