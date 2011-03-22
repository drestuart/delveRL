# External imports
import libtcodpy as libtcod

# Handle key-presses
def handle_keys():
    global fov_recompute

    #key = libtcod.console_check_for_keypress()
    key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED)

    if key.vk == libtcod.KEY_ENTER and libtcod.KEY_ALT:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE:
        return 'exit'  #exit game
 
    if game_state == 'playing':
    #movement keys

        if key.vk == libtcod.KEY_UP:
            player_move_or_attack(0, -1)
 
        elif key.vk == libtcod.KEY_DOWN:
            player_move_or_attack(0, 1)
 
        elif key.vk == libtcod.KEY_LEFT:
             player_move_or_attack(-1, 0)
 
        elif key.vk == libtcod.KEY_RIGHT:
            player_move_or_attack(1, 0)

        else:
            #test for other keys
            key_char = chr(key.c)
 
            if key_char == ',':
                #pick up an item
                for object in objects:  #look for an item in the player's tile
                    if (object.x == player.x 
                        and object.y == player.y 
                        and object.item):

                        object.item.pick_up()
                        break

            if key_char == 'i':
                #show the inventory; if an item is selected, use it
                chosen_item = inventory_menu('Press the key next to an item to use it, or any other to cancel.\n')
                if chosen_item is not None:
                    chosen_item.use()
                    
            if key_char == 'd':
                #show the inventory; if an item is selected, drop it
                chosen_item = inventory_menu('Press the key next to an item to drop it, or any other to cancel.\n')
                if chosen_item is not None:
                    chosen_item.drop()

            return 'didnt-take-turn'
   