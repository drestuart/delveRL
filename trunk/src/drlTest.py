# A testing module.  May well be all messy and stuff.

import libtcodpy as libtcod
from TileClass import *
from MapClass import *
from PlayerClass import *
import os


def handle_keys():
    #key = libtcod.console_check_for_keypress()  #real-time
    key = libtcod.console_wait_for_keypress(True)  #turn-based
    
    if key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
 
 
FONTS_DIR = "../fonts"
 
#actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 69  # Dudes!
 
LIMIT_FPS = 20  #20 frames-per-second maximum

libtcod.console_set_custom_font(os.path.join(FONTS_DIR, 'arial10x10.png'), 
                                libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'delveRL', False)
libtcod.sys_set_fps(LIMIT_FPS)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

map = LevelMap(MAP_WIDTH, MAP_HEIGHT)
map.createRooms()
map.placeCreatures(3)

cr1 = Creature('orc1', 10, map, baseSymbol = 'o')
cr2 = Creature('goblin2', 10, map, baseSymbol = 'g')
cr3 = Creature('giant3', 10, map, baseSymbol = 'G')
cr4 = Creature('dragon4', 10, map, baseSymbol = 'D')

map.placeCreature(cr1)
map.placeCreature(cr2)
map.placeCreature(cr3)
map.placeCreature(cr4)

player = Player(map)
map.placeCreature(player)
 
while not libtcod.console_is_window_closed():
 
    map.draw(con)
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush()
    map.clear(con)
    
    #if handle_keys():
    #    break
     
    map.passTime()
    
    
    