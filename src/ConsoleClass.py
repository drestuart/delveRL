# External imports
import libtcodpy as libtcod

from GetSetClass import *

# Terminal size consts
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

#sizes and coordinates relevant for the GUI
BAR_WIDTH = 20
PANEL_HEIGHT = 7
PANEL_Y = SCREEN_HEIGHT - PANEL_HEIGHT

# Message bar position and size
MSG_X = BAR_WIDTH + 2
MSG_WIDTH = SCREEN_WIDTH - BAR_WIDTH - 2
MSG_HEIGHT = PANEL_HEIGHT - 1



def render_bar(x, y, total_width, name, value, maximum, bar_color, back_color):
    #render a bar (HP, experience, etc). first calculate the width of the bar
    bar_width = int(float(value) / maximum * total_width)
 
    #render the background first
    libtcod.console_set_background_color(panel, back_color)
    libtcod.console_rect(panel, x, y, total_width, 1, False)
 
    #now render the bar on top
    libtcod.console_set_background_color(panel, bar_color)
    if bar_width > 0:
        libtcod.console_rect(panel, x, y, bar_width, 1, False)

    #finally, some centered text with the values
    libtcod.console_set_foreground_color(panel, libtcod.white)
    libtcod.console_print_center(panel, x + total_width / 2, 
                                 y, libtcod.BKGND_NONE,
                                 name + ': ' + str(value) + '/' + str(maximum))

def message(new_msg, color = libtcod.white):
    #split the message if necessary, among multiple lines
    new_msg_lines = textwrap.wrap(new_msg, MSG_WIDTH)
 
    for line in new_msg_lines:
        #if the buffer is full, remove the first line to make room for the new one
        if len(game_msgs) == MSG_HEIGHT:
            del game_msgs[0]
 
        #add the new line as a tuple, with the text and the color
        game_msgs.append( (line, color) )

def get_names_under_mouse():
    #return a string with the names of all objects under the mouse
    mouse = libtcod.mouse_get_status()
    (x, y) = (mouse.cx, mouse.cy)
    #create a list with the names of all objects at the mouse's
    #coordinates and in FOV
    names = [obj.name for obj in objects 
             if obj.x == x and obj.y == y 
             and libtcod.map_is_in_fov(fov_map, obj.x, obj.y)]
    names = ', '.join(names)  #join the names, separated by commas
    return names.capitalize()



# Draw everything!

def render_all():
    global fov_map, color_dark_wall, color_light_wall
    global color_dark_ground, color_light_ground
    global fov_recompute

    if fov_recompute:
        #recompute FOV if needed (the player moved or something)
        fov_recompute = False
        libtcod.map_compute_fov(fov_map, player.x, player.y, 
                                TORCH_RADIUS, FOV_LIGHT_WALLS, FOV_ALGO)

    # Draw the map!
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall = map[x][y].block_sight

                if not visible:
                #if it's not visible right now, the player can only
                #see it if it's explored
                    if map[x][y].explored:

                    #it's out of the player's FOV
                        if wall:
                            #libtcod.console_set_back(con, x, y, 
                             #                        color_dark_wall, 
                              #                       libtcod.BKGND_SET)
                            libtcod.console_put_char_ex(con, x, y, '#', 
                                                        color_dark_wall, 
                                                        libtcod.dark_blue)
                        else:
                            #libtcod.console_set_back(con, x, y, 
                             #                        color_dark_ground, 
                              #                       libtcod.BKGND_SET)
                            libtcod.console_put_char_ex(con, x, y, '.', 
                                                        color_dark_ground, 
                                                        libtcod.dark_blue)
                else:
                    #it's visible
                    if wall:
                        #libtcod.console_set_back(con, x, y, 
                         #                        color_light_wall, 
                          #                       libtcod.BKGND_SET )
                        libtcod.console_put_char_ex(con, x, y, '#', 
                                                    color_light_wall,
                                                    libtcod.dark_blue)

                        
                    else:
                        #libtcod.console_set_back(con, x, y, 
                         #                        color_light_ground,
                          #                       libtcod.BKGND_SET )

                        libtcod.console_put_char_ex(con, x, y, '.', 
                                                    color_light_ground, 
                                                    libtcod.dark_blue)

                    #since it's visible, explore it
                    map[x][y].explored = True


    #draw all objects in the list, except the player. we want it to
    #always appear over all other objects! so it's drawn later.
    for object in objects:
        if object != player:
            object.draw()
    player.draw()
   

    #blit the contents of "con" to the root console and present it
    libtcod.console_blit(con, 0, 0, MAP_WIDTH, MAP_HEIGHT, 0, 0, 0)

    #prepare to render the GUI panel
    libtcod.console_set_background_color(panel, libtcod.black)
    libtcod.console_clear(panel)

    #print the game messages, one line at a time
    y = 1
    for (line, color) in game_msgs:
        libtcod.console_set_foreground_color(panel, color)
        libtcod.console_print_left(panel, MSG_X, y, libtcod.BKGND_NONE, line)
        y += 1
 
    #show the player's stats
    render_bar(1, 1, BAR_WIDTH, 'HP', player.fighter.hp, player.fighter.max_hp,
        libtcod.light_red, libtcod.darker_red)
 
    #display names of objects under the mouse
    libtcod.console_set_foreground_color(panel, libtcod.light_gray)
    libtcod.console_print_left(panel, 1, 0, libtcod.BKGND_NONE,
                               get_names_under_mouse())

    #blit the contents of "panel" to the root console
    libtcod.console_blit(panel, 0, 0, SCREEN_WIDTH, PANEL_HEIGHT, 0, 0, PANEL_Y)

    libtcod.console_flush()

