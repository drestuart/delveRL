# External imports
import libtcodpy as libtcod

# Internal imports
from DungeonFeatureClass import *

# Constants

# Wall and ground colors
color_dark_wall = libtcod.Color(0, 0, 100)
color_light_wall = libtcod.Color(130, 110, 50)
color_dark_ground = libtcod.Color(50, 50, 150)
color_light_ground = libtcod.Color(200, 180, 50)

# The Tile class

class Tile:
    #a tile of the map and its properties
    def __init__(self, block_move = False, block_sight = False, base_symbol = '.', 
                 color = color_light_ground, background = libtcod.BKGND_NONE, 
                 feature = None):
        
        self.block_move = block_move
        self.block_sight = block_sight
        self.base_symbol = base_symbol
        self.color = color
        self.background = background
        
        self.objects = []      # The objects on this tile 
        self.creature = None   #The creature on this tile.  The ONE creature, by the way.
        
        if feature:
            self.feature = feature
            
    def toDraw(self):
        # Returns a tuple of the tile's symbol, color, and background for the drawing functionality 
        return self.symbol(), self.color, self.background
    
    def blocks_move(self):
         # Determine whether creatures can see through this square.
        
        if self.creature:
            # Blocked by creature.  All creatures block movement
            return True 
        
        blocks = self.block_move
                
        if self.feature:
            # If there's a dungeon feature, determine if it blocks movement before returning.  
            # This also accounts for the case of a non-blocking feature in a blocking square, which seems unlikely.
            blocks = blocks and self.feature.block_sight
                
        return blocks
    
    def blocks_sight(self):
        # Determine whether creatures can see through this square.  Similar to the above blocks_move()
        
        blocks = self.block_sight
        if self.creature:
            # Blocked by creature.  Not all creatures block sight
            blocks = blocks and self.creature.block_sight 
        
        elif self.feature:
            # If there's a dungeon feature, determine if it blocks sight.  
            # This also accounts for the case of a non-blocking feature in a blocking square, which seems unlikely.
            blocks = blocks and self.feature.block_sight
                
        return blocks
    
    def add_object(self, object):
        # Put an object into this tile, if possible.
        if not self.block_move:
            self.objects.append(object)
    
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
        
    def symbol(self):
        # Determine which symbol to use to draw this tile
        if self.creature and self.creature.is_visible():
            return creature.symbol
        
        elif self.feature and self.feature.is_visible():
            return feature.symbol
        
        elif self.objects:
            return self.object[0].symbol
        
        else:
            return self.base_symbol
        
        
        
            
def main():
    tile = Tile(symbol = 'x')  
    print tile.color, tile.blocks_move(), tile.blocks_sight()
            
if __name__ == '__main__':
    main()

