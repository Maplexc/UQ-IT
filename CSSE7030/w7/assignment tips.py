# gui
# controller
# model
# record - listen again


# model
# position

# move
# attack
# pickup
# putdowm

# Item
#   name
#   position

SQ_CLOSE = 1600

def close_to(p1,p2):
    """
    p1 (tuple): position of first point (x1,y2)
    p2 (tuple): position of second point (x2,y2)
    """
    x1, y1 = p1 # unpack p1
    x2, y2 = p2
    return (x1-x2)**2 + (y1-y2)**2 < SQ_CLOSE
    # return True if close, False if not

class Character(object):
    # set all the character
    def __init__(self, x, y, name):
        # self._x = x
        # self._y = y
        # another way below
        self._x, self._y = x, y
        self._name = name
        self._inventory = [] # what is in the backpack - list
        self._holding = None # what is holding in the hand (None to start, or [] is also work)

    def get_name(self):
        return self._name
    
    def get_position(self):
        return (self._x, self._y)
    
    def get_inventory(self):
        return self._inventory

    def get_holding(self):
        return self._holding
    
    def take(self, item):
        self._inventory.append(item)
        item.set_taken(True)
    
    def hold(self, index):
        # index - the index of the item that taken up
        if 0 <= index < len(self._inventory):
            self._holding = self._inventory[index]
    
    def drop(self, index):
        if 0 <= index < len(self._inventory):
            item = self._inventory.pop(index)
            x, y = self.get_position()
            item.set_position(x, y)
            item.set_taken(False)
            if item == self._holding:
                self._holding = None
                # if not holding anything, None given to self._holding
    
    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def __repr__(self):
        return "Char name: {0}  Pos: {1}  Inventory: {2}".format(self.get_name(), self.get_position(), self.get_inventory())


# class Item
class Item(object):
    def __init__(self, x, y, name):
        self._x, self._y = x, y
        self._name = name
        self._taken = False # initially the item are not be taken, so False at the begining

    def get_position(self):
        return (self._x, self._y)

    def set_position(self, x, y):
        self._x, self._y = x, y

    def get_name(self):
        return self._name

    
    def set_taken(self,t):
        self._taken = t

    def is_taken(self):
        return self._taken

    def __str__(self):
        return self.get_name()
    
    def __repr__(self):
        return "Item name: {0}  Pos:{1}  Taken? {2}".format(self.get_name(), self.get_position(), self.is_taken())
    






