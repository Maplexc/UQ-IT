
# Adventure game

# Character
#   name
#   health
#   armour
#   inventory
#   position

#   move
#   attack
#   pickup
#   put down

# Item
#   name
#   position

# Model

SQ_CLOSE = 1600

def close_to(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1 - x2)**2 + (y1 - y2)**2 < SQ_CLOSE

class Character(object):
    def __init__(self, x, y, name):
        self._x, self._y = x, y
        self._name = name
        self._inventory = []
        self._holding = None

    def get_name(self):
        return self._name
    
    def get_position(self):
        return (self._x, self._y)

    def get_inventory(self):
        return self._inventory

    def get_holding(self):
        return self._holding

    def take(self, item):
        self._inventory.append(item) # item is an object from the Item class
        item.set_taken(True)

    def hold(self, index):
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
            
    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def __repr__(self):
        return "Char name: {0}  Pos: {1}  Inventory: {2}".format(self.get_name(),
                                                                 self.get_position(),
                                                                 self.get_inventory())

class Item(object):
    def __init__(self, x, y, name):
        self._x, self._y = x, y
        self._name = name
        self._taken = False

    def get_name(self):
        return self._name
    
    def set_position(self, x, y):
        self._x, self._y = x, y

    def get_position(self):
        return (self._x, self._y)

        
    def set_taken(self, t):
        self._taken = t

    def is_taken(self):
        return self._taken

    def __str__(self):
        return self.get_name()
    
    def __repr__(self):
        return "Item name: {0} Pos: {1} taken? {2}".format(self.get_name(),
                                                           self.get_position(),
                                                           self.is_taken()) 



class Model(object):
    def __init__(self):
        self._char = Character(50, 50, "player")

        self._items = [Item(400, 50, "sword"),
                       Item(50, 400, "potion"),
                       Item(600, 400, "dagger")]

    def get_character(self):
        return self._char

    def get_items(self):
        return self._items

    def character_take_item(self):
        # interaction take place
        char_pos = self._char.get_position()
        for item in self._items:
            item_pos = item.get_position()
            # get the position of item, compare it with the position with character to check whether they are close to each other
            if close_to(char_pos, item_pos) and not item.is_taken():
                # not item.is_taken() means that when item is not taken
                self._char.take(item)
                                                
    def __repr__(self):
        return "{0}, {1}".format(self._char, self._items)
    








    
