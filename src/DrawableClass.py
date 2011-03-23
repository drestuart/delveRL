# Parent class for objects that will be drawn in a console

import libtcodpy as libtcod

class Drawable:
    
    
    
    def clear(self)
        #erase the character that represents this object
        if libtcod.map_is_in_fov(fov_map, self.x, self.y):
            libtcod.console_put_char_ex(con, self.x, self.y, '.', 
                                        libtcod.white, libtcod.dark_blue)