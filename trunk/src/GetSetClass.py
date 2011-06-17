class GetSet(object):
    
    def __setattr__(self, name, value):
        print "Use set functions instead!  Direct variable setting for this object is deprecated!"
        print "Setting", name, "to", value, "in", self.__class__
        self.__dict__[name] = value
    