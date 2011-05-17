# The map class.  This will contain the code for creating and displaying maps.
# The plan is to have two maps: the *actual* level map, and the player's map
# showing what they know/remember about the level.

# External imports
#import random
import libtcodpy as libtcod

# Internal imports
from TileClass import *
from CreatureClass import *
from GetSetClass import *


# Max monsters per room
MAX_ROOM_MONSTERS = 3

# Max items per room
MAX_ROOM_ITEMS = 2

# Field of view constants
FOV_ALGO = 0  #default FOV algorithm
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10
fov_recompute = True

# Map dimensions
MAP_WIDTH = 80
MAP_HEIGHT = 50

# Some dungeon generation constants
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30


# The Rectangle class
class Rect:
    #a rectangle on the map. used to characterize a room.
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return (center_x, center_y)
 
    def intersect(self, other):
        #returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)
        
        
class Map(GetSet):
        
    def __init__(self, width, height, name = '', depth = 0):
        self.WIDTH = width
        self.HEIGHT = height
        self.name = name
        self.depth = depth

        #fill map with "wall" tiles

        self.tiles = [[ Tile(x, y, blockMove = True, blockSight = True, baseSymbol = '#', 
                             baseColor = colorDarkWall, baseDescription = 'Rock wall') 
                             for y in range(self.HEIGHT) ]
                             for x in range(self.WIDTH) ]
        
        self.tileList = []
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                self.tileList.append(self.tiles[x][y])
        
    def createRooms(self):
        '''Add some rooms to the map'''
        rooms = []
        num_rooms = 0
     
        # Make some rooms
        for r in range(MAX_ROOMS):
            #random width and height
            w = libtcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
            h = libtcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
    
            #random position without going out of the boundaries of the map
            x = libtcod.random_get_int(0, 0, self.WIDTH - w - 1)
            y = libtcod.random_get_int(0, 0, self.HEIGHT - h - 1)
    
            #"Rect" class makes rectangles easier to work with
            new_room = Rect(x, y, w, h)
     
            #run through the other rooms and see if they intersect with this one
            failed = False
            for other_room in rooms:
                if new_room.intersect(other_room):
                    failed = True
                    break
    
            if not failed:
                #this means there are no intersections, so this room is valid
     
                #"paint" it to the map's tiles
                self.createRoom(new_room)
    
                #add some contents to this room, such as monsters
                self.placeObjects(new_room)
     
                #center coordinates of new room, will be useful later
                (new_x, new_y) = new_room.center()
         
                if num_rooms >= 1:
                    #all rooms after the first:
                    #connect it to the previous room with a tunnel
     
                    #center coordinates of previous room
                    (prev_x, prev_y) = rooms[-1].center()
     
                    #draw a coin (random number that is either 0 or 1)
                    if libtcod.random_get_int(0, 0, 1) == 1:
                        #first move horizontally, then vertically
                        self.createHTunnel(prev_x, new_x, prev_y)
                        self.createVTunnel(prev_y, new_y, new_x)
                    else:
                        #first move vertically, then horizontally
                        self.createVTunnel(prev_y, new_y, prev_x)
                        self.createHTunnel(prev_x, new_x, new_y)
    
     
                #finally, append the new room to the list
                rooms.append(new_room)
                num_rooms += 1

    def passTime(self, turns = 1):
        print "tick"
        
        for i in range(turns):
            creatures = []
            
            for x in range(self.WIDTH):
                for y in range(self.HEIGHT):
                    self.tiles[x][y].passTime()
                    cr = self.tiles[x][y].creature
                    
                    if cr is not None:
                        creatures.append(cr)
                        
            for cr in creatures:
                cr.passTime()
                        
                        
    # Create a room
    def createRoom(self, room):
        #go through the tiles in the rectangle and make them floors
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y] = Tile(x, y)  # Default is a floor tile

    # Carve out a horizontal tunnel
    def createHTunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y] = Tile(x, y)  # Default is a floor tile

    # Carve out a vertical tunnel
    def createVTunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y] = Tile(x, y)  # Default is a floor tile


    # Test if a square is blocked
    def isBlocked(self, x, y):
        return self.tiles[x][y].blocksMove()
    



    # Add some monsters! Rawr!
    def placeObjects(self, room):
        # Disable for now
        return
        #choose random number of monsters
        num_monsters = libtcod.random_get_int(0, 0, MAX_ROOM_MONSTERS)
     
        for i in range(num_monsters):
            #choose random spot for this monster
            x = libtcod.random_get_int(0, room.x1+1, room.x2-1)
            y = libtcod.random_get_int(0, room.y1+1, room.y2-1)
    
            #only place it if the tile is not blocked
            if not isBlocked(x, y):
     
                #80% chance of getting an orc
                if libtcod.random_get_int(0, 0, 100) < 80:  
                    
                    #create an orc
                    fighter_component = Fighter(hp=10, defense=0, power=3, 
                                                death_function=monster_death)
                    ai_component = BasicMonster()
     
                    monster = Object(x, y, 'o', 'orc', libtcod.desaturated_green,
                        blocks=True, fighter=fighter_component, ai=ai_component)
                else:
                    #create a troll
                    fighter_component = Fighter(hp=16, defense=1, power=4, 
                                                death_function=monster_death)
                    ai_component = BasicMonster()
     
                    monster = Object(x, y, 'T', 'troll', libtcod.darker_green,
                        blocks=True, fighter=fighter_component, ai=ai_component)
    
     
                objects.append(monster)
    
        #choose random number of items
        num_items = libtcod.random_get_int(0, 0, MAX_ROOM_ITEMS)
     
        for i in range(num_items):
            #choose random spot for this item
            x = libtcod.random_get_int(0, room.x1+1, room.x2-1)
            y = libtcod.random_get_int(0, room.y1+1, room.y2-1)
     
            #only place it if the tile is not blocked
            if not isBlocked(x, y):
                dice = libtcod.random_get_int(0, 0, 100)
                if dice < 70:
                    #create a healing potion (70% chance)
                    item_component = Item(use_function=cast_heal)
     
                    item = Object(x, y, '!', 'healing potion', libtcod.violet, 
                                  item=item_component)
                    #print "Placed healing potion at ", str(x), ", ", str(y)
                elif dice < 70+10:
                    #create a lightning bolt scroll (10% chance)
                    item_component = Item(use_function=cast_lightning)
     
                    item = Object(x, y, '?', 'scroll of lightning bolt', libtcod.light_yellow, item=item_component)
                
                elif dice < 70+10+10:
                    #create a fireball scroll (10% chance)
                    item_component = Item(use_function=cast_fireball)
     
                    item = Object(x, y, '#', 'scroll of fireball', libtcod.light_yellow, item=item_component)
                
                else:
                    #create a confuse scroll (10% chance)
                    item_component = Item(use_function=cast_confuse)
     
                    item = Object(x, y, '?', 'scroll of confusion', libtcod.light_yellow, item=item_component)
    
                objects.append(item)
                
    # Draw that map!
    def draw(self, con):
#        libtcod.console_set_foreground_color(con, self.color())
#        libtcod.console_put_char(con, self.x, self.y, self.symbol(), self.background())

        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                #try:
                    symbol, color, background = self.tiles[x][y].toDraw()
                    libtcod.console_set_foreground_color(con, color)
                    libtcod.console_put_char(con, x, y, symbol, background)
                #except:
                #    print symbol, color, background
                    
                    
    # Erase that map!
    def clear(self, con):
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                libtcod.console_put_char(con, x, y, ' ', libtcod.BKGND_NONE)
                
    def getRandOpenSpace(self):
        '''Get a random open square on the map'''
        while True:
            randx = libtcod.random_get_int(0, 0, self.WIDTH - 1)
            randy = libtcod.random_get_int(0, 0, self.HEIGHT - 1)
        
            if not self.isBlocked(randx, randy):
                return randx, randy
            
    def placeCreature(self, creature):
        while True:
            x, y = self.getRandOpenSpace() 
        
            if not self.tiles[x][y].creature:
                self.tiles[x][y].creature = creature
                creature.x = x
                creature.y = y
                break
            
    def placeCreatures(self, num_creatures):
        for i in range(num_creatures):
            self.placeCreature(randomCreature(self))
                
def main():
        map = Map(40, 40)

if __name__ == '__main__':
        main()
                
                
#####################################################
#
# Old functions!
#
#####################################################

def target_tile(max_range=None):
    #return the position of a tile left-clicked in player's FOV (optionally in a range), or (None,None) if right-clicked.
    while True:
        #render the screen. this erases the inventory and shows the names of objects under the mouse.
        render_all()
        libtcod.console_flush()
 
        key = libtcod.console_check_for_keypress()
        mouse = libtcod.mouse_get_status()  #get mouse position and click status
        (x, y) = (mouse.cx, mouse.cy)
 
        #accept the target if the player clicked in FOV, and in case a range is specified, if it's in that range
        if (mouse.lbutton_pressed and libtcod.map_is_in_fov(fov_map, x, y) and
            (max_range is None or player.distance(x, y) <= max_range)):
            return (x, y)
                    
        if mouse.rbutton_pressed or key.vk == libtcod.KEY_ESCAPE:
            return (None, None)  #cancel if the player right-clicked or pressed Escape
        
def target_monster(max_range=None):
    #returns a clicked monster inside FOV up to a range, or None if right-clicked
    while True:
        (x, y) = target_tile(max_range)
        if x is None:  #player cancelled
            return None
 
        #return the first clicked monster, otherwise continue looping
        for obj in objects:
            if obj.x == x and obj.y == y and obj.fighter and obj != player:
                return obj        
        

def closest_monster(max_range):
    #find closest enemy, up to a maximum range, and in the player's FOV
    closest_enemy = None
    closest_dist = max_range + 1  #start with (slightly more than) maximum range
 
    for object in objects:
        if (object.fighter and not object == player 
            and libtcod.map_is_in_fov(fov_map, object.x, object.y)):

            #calculate distance between this object and the player
            dist = player.distance_to(object)
            if dist < closest_dist:  #it's closer, so remember it
                closest_enemy = object
                closest_dist = dist
    return closest_enemy

