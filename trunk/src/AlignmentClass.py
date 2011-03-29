# The Aligment class.  Used to keep track of the ethical and moral axes that
# underpin the theological workings of the world.

ethical = ("L", "N", "C")
moral = ("G", "N", "E")

class alDistanceTable:
    table = {"LL":0, "LN":1, "LC":2, "CN":1, "CC":0, "NN":0,
             "GG":0, "GN":1, "GE":2, "NE":1, "EE":0}
    
    def get(self, align1, align2):
        dist = (self.table.get(align1 + align2) or
                self.table.get(align2 + align1))
        
        if dist == None:
            return None
        else:
            return dist
        
distanceTable = alDistanceTable()

class AlignComponent:
    def __init__(self, align):
        if (align in ethical):
            self.align = align
            self.type = "ethical"
        elif (align in moral):
            self.align = align
            self.type = "moral"
        else:
            raise ValueError("invalid alignment specified: " + align)
        
    def distance(self, other):
        return distanceTable.get(self.align, other.align)
    
    def __repr__(self):
        return self.align
        
        

class Alignment:
    # Initialize the alignment object with a string, and optionally a starting
    # piety level, and a bool to indicate whether this is a static alignment
    # (for monsters) or should update itself (for players)
    def __init__(self, align, piety = 10, updates = False):
        if (not align.__class__ is str) or (len(align) != 2):
            raise ValueError("invalid alignment specified: " + align)
        else:
            ac1, ac2 = AlignComponent(align[0]), AlignComponent(align[1])

        if ac1.type == ac2.type:
            raise ValueError("invalid alignment specified: " + align)
        else:
            if ac1.type == 'ethical':
                self.ethical = ac1
                self.moral = ac2
            else:
                self.ethical = ac2
                self.moral = ac1
                
        self.peity = piety
        self.updates = updates
        
    def distance(self, other):
        return self.ethical.distance(other.ethical) + self.moral.distance(other.moral)

def alDistance(al1, al2):
    return al1.distance(al2)

def main():
    NE = Alignment("NE")
    CG = Alignment("CG")
    print distanceTable.get("L", "C")
    print NE.distance(CG)
    print NE.distance(NE)


if __name__ == '__main__':
    main()







