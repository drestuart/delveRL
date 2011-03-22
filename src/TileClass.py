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
    def __init__(self, block_move = False, block_sight = False, symbol = '.', 
                 color = color_light_ground, background = libtcod.BKGND_NONE, 
                 feature = None):
        
        self.block_move = block_move
        self.block_sight = block_sight
        self.symbol = symbol
        self.color = color
        self.background = background
        
        if feature:
            self.feature = feature
            
    def toDraw(self): 
        return self.symbol, self.color, self.background
    
    def blocks_move(self):
        return self.block_move
    
    def blocks_sight(self):
        return self.block_sight
                
            
def main():
    tile = Tile(symbol = 'x')  
    print tile.color
            
if __name__ == '__main__':
    main()

