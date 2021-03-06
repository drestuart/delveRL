# External imports
import libtcodpy as libtcod

from GetSetClass import *

# The Object class.  How much more general can you get?

class Object(GetSet):
    #this is a generic object: the player, a monster, an item, the
    #stairs...  it's always represented by a character on screen.
    def __init__(self, x, y, char, name, color, 
                 blocksSight=False, blocksMove=False):

        self.x = x
        self.y = y
        self.char = char
        self.name = name
        self.color = color
        self.blocksSight = blocksSight
        self.blocksMove = blocksMove
            
    def distance(self, x, y):
        # Return the distance to some coordinates.  For now we're using the
        # Euclidean distance, but maybe switch to A* distance later?
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)


    def move(self, dx, dy):
        if not isBlocked(self.x + dx, self.y + dy):

            #move by the given amount
            self.x += dx
            self.y += dy

#    def send_to_back(self):
#        #make this object be drawn first, so all others appear above
#        #it if they're in the same tile.
#        global objects
#        objects.remove(self)
#        objects.insert(0, self)

 
#    def draw(self):
#        # If we can see the object:
#        if libtcod.map_is_in_fov(fov_map, self.x, self.y):
#
#            #set the color and then draw the character that represents
#            #this object at its position
#            libtcod.console_set_foreground_color(con, self.color)
#            libtcod.console_put_char(con, self.x, self.y, 
#                                     self.char, #self.color, 
#                                     libtcod.BKGND_NONE)
#
#
#        else:
#            # If we've seen the item, but it's out of view now
#            if map[self.x][self.y].explored:
#                libtcod.console_set_foreground_color(con, libtcod.dark_grey)
#                libtcod.console_put_char_ex(con, self.x, self.y, 
#                                            self.char, libtcod.dark_grey, 
#                                         #libtcod.BKGND_NONE)
#                                            libtcod.dark_blue)
# 
#    def clear(self):
#        #erase the character that represents this object
#        if libtcod.map_is_in_fov(fov_map, self.x, self.y):
#            libtcod.console_put_char_ex(con, self.x, self.y, '.', 
#                                        libtcod.white, libtcod.dark_blue)

    def moveTowards(self, target_x, target_y):
        #vector from this object to the target, and distance
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
 
        #normalize it to length 1 (preserving direction), then round it and
        #convert to integer so the movement is restricted to the map grid
        dx = int(round(dx / distance))
        dy = int(round(dy / distance))
        self.move(dx, dy)

    def distanceTo(self, other):
        #return the distance to another object
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
    
    def passTime(self, turns = 1):
        '''Pass some time on the object.  Does nothing by default.  Will override in subclasses'''
        pass
        
        
        
