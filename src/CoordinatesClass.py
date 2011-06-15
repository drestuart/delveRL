# A class to hold coordinate (x, y) coordinates.  The idea is the make the whole thing order-independent.

# Internal imports
from GetSetClass import *

class Coordinates(GetSet):
     
    def __init__(self, **kwargs):
        self.__dict__['x'] = kwargs['x']
        self.__dict__['y'] = kwargs['y']
        
    def setX(self, x):
        self.__dict__['x'] = x
    
    def setY(self, y):
        self.__dict__['y'] = y
        
    def setXY(self, **kwargs):
        self.__dict__['x'] = kwargs['x']
        self.__dict__['y'] = kwargs['y']
        
    def getXY(self):
        return {'x' : self.x, 'y' : self.y}
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def __repr__(self):
        return "Coordinates(x = " + str(self.x) + ", y = " + str(self.y) + ")"
    
    def __str__(self):
        return str( (self.x, self.y) )
    
    def __add__(self, other):
        return Coordinates(self['x'] + other['x'], self['y'] + other['y'])
    
    def __getitem__(self, item):
        if item in ['x', 'y']:
            return self.__dict__[item]
        
        else:
            raise ValueError(item)
    
    
    
def main():
    place1 = Coordinates(x = 3, y = 4)
    print place1.getXY()
    print place1
    
    place1.setXY(x = 5, y = 5)
    print place1
    print place1.__repr__()

if __name__ == '__main__':
    main()