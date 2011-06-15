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
        
    def getXY(self):
        return self.x, self.y
    
    def __repr__(self):
        return "Coordinates(" + str(self.x) + "," + str(self.y) + ")"
    
    def __str__(self):
        return str(self.getXY())
    
    
    
def main():
    place1 = Coordinates(3,4)
    print place1.getXY()
    print place1
    
    place1.setXY(5,5)
    print place1
    print place1.__repr__()

if __name__ == '__main__':
    main()