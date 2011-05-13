############################################################
#
# Old stuff!
# THIS MODULE CONDEMNED
# 
############################################################


# External imports
import libtcodpy as libtcod
import math
import textwrap

# Internal imports
from ConsoleClass import *
from CreatureClass import *
from ItemClass import *
from MapClass import *
from ObjectClass import *
from SpellClass import *
from TileClass import *
from keys import *

############################################################
#
# Functions
# 
############################################################

def player_death(player):
    #the game ended!
    global game_state
    message('You died!', libtcod.red)
    game_state = 'dead'
 
    #for added effect, transform the player into a corpse!
    player.char = '%'
    player.color = libtcod.dark_red
 
def monster_death(monster):
    #transform it into a nasty corpse! it doesn't block, can't be
    #attacked and doesn't move
    message(monster.name.capitalize() + ' is dead!', libtcod.orange)
    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    monster.send_to_back()





# Player: Move or attack!
def player_move_or_attack(dx, dy):
    global fov_recompute
 
    #the coordinates the player is moving to/attacking
    x = player.x + dx
    y = player.y + dy
 
    #try to find an attackable object there
    target = None
    for object in objects:
        if object.fighter and object.x == x and object.y == y:
            target = object
            break
 
    #attack if target found, move otherwise
    if target is not None:
        player.fighter.attack(target)

    else:
        player.move(dx, dy)
        fov_recompute = True










def main():

    
    ############################################################
    #
    # Set up stuff and enter main loop
    #
    ############################################################
    
    # Globals.  Sorry everyone.
    global objects, con, panel, player, inventory, game_state, player_action, game_msgs, fov_map
    
    
    #create the list of game messages and their colors, starts empty
    
    game_msgs = []
    
    # Select font -- arial 10pt
    libtcod.console_set_custom_font('../fonts/arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    
    # Open window.  The parameters are: width, height (in characters?),
    # title, and whether to full-screen or not.
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'leRogueLike 0.0.0', False)
    
    # The main console!
    con = libtcod.console_new(MAP_WIDTH, MAP_HEIGHT)
    
    # The GUI panel
    panel = libtcod.console_new(SCREEN_WIDTH, PANEL_HEIGHT)
    
    
    # Limit framerate, if you *really* have to make a realtime RL
    libtcod.sys_set_fps(LIMIT_FPS)
    
    #create object representing the player
    fighter_component = Fighter(hp=30, defense=2, power=5,
                                death_function=player_death)
    player = Object(0, 0, '@', 'player', libtcod.white, blocks=True, fighter=fighter_component)
     
    #the list of objects starting with the player
    objects = [player]

    
    # The inventory
    inventory = []
    
    
    
    # Make the map!
    make_map()
    
    # Give libtcod the map?
    fov_map = libtcod.map_new(MAP_WIDTH, MAP_HEIGHT)
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            libtcod.map_set_properties(fov_map, x, y, 
                                       not map[x][y].blocked, 
                                       not map[x][y].block_sight)
    
    
    # Initialize the player status variables
    game_state = 'playing'
    player_action = None
    
    #a warm welcoming message!
    message('Welcome stranger! Prepare to perish in the Tombs of the Ancient Kings.', libtcod.red)
    
    # Run the game while the window is open
    while not libtcod.console_is_window_closed():
        # Genius goes here
            
        render_all()
     
        
     
        #erase all objects at their old locations, before they move
        for object in objects:
            object.clear()
     
        #handle keys and exit game if needed
        player_action = handle_keys()
        if player_action == 'exit':
            break
    
        #let monsters take their turn
        if game_state == 'playing' and player_action != 'didnt-take-turn':
            for object in objects:
                if object.ai:
                    object.ai.take_turn()



if __name__ == '__main__':
    main() 