# External imports
import libtcodpy as libtcod

# Internal imports
from DungeonFeatureClass import *
from InventoryClass import *

# Constants

# Wall and ground colors
color_dark_wall = libtcod.Color(0, 0, 100)
color_light_wall = libtcod.Color(130, 110, 50)
color_dark_ground = libtcod.Color(50, 50, 150)
color_light_ground = libtcod.Color(200, 180, 50)

# The Tile class

class Tile:
    #a tile of the map and its properties
    def __init__(self, x = 0, y = 0, block_move = False, block_sight = False, base_symbol = '.', 
                 base_color = color_light_ground, base_background = libtcod.BKGND_NONE, 
                 feature = None, base_description = "floor"):
        
        self.x = x
        self.y = y
        self.block_move = block_move
        self.block_sight = block_sight
        self.base_symbol = base_symbol
        self.base_color = base_color
        self.base_description = base_description
        self.base_background = base_background
        
        self.objects = ItemInventory()      # The objects on this tile 
        self.creature = None   #The creature on this tile.  The ONE creature, by the way.
        
        self.feature = feature
            
    def toDraw(self):
        # Returns a tuple of the tile's symbol, color, and background for the
        # drawing functionality
        return self.symbol(), self.color(), self.background()
    
    def blocks_move(self):
         # Determine whether creatures can see through this square.
        
        if self.creature:
            # Blocked by creature.  All creatures block movement
            return True 
        
        blocks = self.block_move
                
        if self.feature:
            # If there's a dungeon feature, determine if it blocks movement
            # before returning. This also accounts for the case of a non-
            # blocking feature in a blocking square, which seems unlikely.
            blocks = blocks and self.feature.block_sight
                
        return blocks
    
    def blocks_sight(self):
        # Determine whether creatures can see through this square.  Similar to
        # the above blocks_move()
        
        blocks = self.block_sight
        if self.creature:
            # Blocked by creature.  Not all creatures block sight
            blocks = blocks and self.creature.block_sight 
        
        elif self.feature:
            # If there's a dungeon feature, determine if it blocks sight. This
            # also accounts for the case of a non-blocking feature in a blocking
            # square, which seems unlikely.
            blocks = blocks and self.feature.block_sight
                
        return blocks
    
    def add_object(self, object):
        # Put an object into this tile, if possible.
        if not self.block_move:
            self.objects.add(object)
    
    def add_objects(self, objects):
        # Put several objects into this tile
        [self.add_object(obj) for obj in objects]
            
    def remove_object(self, index):
        # Take an object from this tile
        obj = self.objects.pop(index)
        return obj
    
    def remove_objects(self, indices):
        # Take some objects from this tile
        return [remove_object(ind) for ind in indices]
    
    def add_creature(self, creature):
        if not (self.block_move and self.creature):
            self.creature = creature
            
    def passTime(self, turns = 1):
        '''Pass some time on the objects and creature on this tile'''
        for obj in self.objects:
            obj.passTime(turns)
            
        if self.creature is not None:
            self.creature.passTime(turns)
        
        
    # Some functions that show what's in the Tile        
    def symbol(self):
        # Determine which symbol to use to draw this tile
        if self.creature and self.creature.is_visible():
            return self.creature.symbol
        
        elif self.feature and self.feature.is_visible():
            return self.feature.symbol
        
        elif self.objects:
            return self.objects[0].symbol
        
        else:
            return self.base_symbol
        
    def color(self):
        # Determine which color to use to draw this tile
        if self.creature and self.creature.is_visible():
            return self.creature.color
        
        elif self.feature and self.feature.is_visible():
            return self.feature.color
        
        elif self.objects:
            return self.objects[0].color
        
        else:
            return self.base_color        

    def background(self):
        # Determine which background to use to draw this tile
        if self.creature and self.creature.is_visible():
            return self.creature.background
        
        elif self.feature and self.feature.is_visible():
            return self.feature.background
                
        else:
            return self.base_background   

    def description(self):
        # Determine which description to use to draw this tile
        if self.creature and self.creature.is_visible():
            return self.creature.description
        
        elif self.feature and self.feature.is_visible():
            return self.feature.description
        
        elif self.objects:
            return self.objects[0].description
        
        else:
            return self.base_description   
    
#    # drawing management stuff. will be moved to the console class?    
#    def draw(self, con):
#        #set the color and then draw the character that represents this object
#        #at its position
#        libtcod.console_set_foreground_color(con, self.color())
#        libtcod.console_put_char(con, self.x, self.y, self.symbol(), self.background)
# 
#    def clear(self, con):
#        #erase the character that represents this object
#        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)
        
        
        
            
def main():
    tile = Tile(base_symbol = 'x', base_description = 'some junk')  
    print tile.color(), tile.symbol(), tile.description()
            
if __name__ == '__main__':
    main()













