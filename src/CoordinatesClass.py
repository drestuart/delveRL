# A class to hold coordinate (x, y) coordinates

# Internal imports
from GetSetClass import *

class Coordinates(GetSet):
     
    def __init__(self, x, y):
        self.__dict__['x'] = x
        self.__dict__['y'] = y
        
    def setX(self, x):
        self.__dict__['x'] = x
    
    def setY(self, y):
        self.__dict__['y'] = y
        
    def setXY(self, x, y):
        self.__dict__['x'] = x
        self.__dict__['y'] = y
        
    def getXY(self, x, y):
        return self.x, self.y