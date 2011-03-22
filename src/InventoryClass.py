# External imports
import libtcodpy as libtcod
from keys import *
from menu import *

INVENTORY_WIDTH = 50

# The inventory menu
def inventory_menu(header):
    #show a menu with each item of the inventory as an option
    if len(inventory) == 0:
        options = ['Inventory is empty.']
    else:
        options = [item.name for item in inventory]
 
    index = menu(header, options, INVENTORY_WIDTH)

    #if an item was chosen, return it
    if index is None or len(inventory) == 0:
        return None
    return inventory[index].item

