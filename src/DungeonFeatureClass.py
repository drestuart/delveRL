

class DungeonFeature:
    # Dummy class right now.  Will eventually represent dungeon features like traps, altars and stairs
    
    def __init__(self, block_sight = False, block_move = False, symbol = '}'):
        self.block_sight = block_sight
        self.block_move = block_move
        self.symbol = symbol