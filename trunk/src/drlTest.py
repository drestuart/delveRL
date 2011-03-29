# A testing module.  May well be all messy and stuff.

import libtcodpy as libtcod
from TileClass import *
from MapClass import *
import os

def handle_keys():
    key = libtcod.console_wait_for_keypress(True)  #turn-based
 
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
 
 
FONTS_DIR = "../fonts"
 
#actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 69  # Dudes!
 
LIMIT_FPS = 20  #20 frames-per-second maximum

libtcod.console_set_custom_font(os.path.join(FONTS_DIR, 'arial10x10.png'), 
                                libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcod.sys_set_fps(LIMIT_FPS)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

map = Map(MAP_WIDTH, MAP_HEIGHT)


 
while not libtcod.console_is_window_closed():
 
    map.draw(con)
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush()
    map.clear(con)
    
    if handle_keys():
        break
    
    
    
    