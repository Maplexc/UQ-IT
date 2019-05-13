def md(x):
    a,b = x
    a,b = a//b, a%b
    return (a,b)

def get_days(years):
    total_days = 0
    while years >= 0:
        total_days += 365
        years -= 1
    return total_days

##years = input("How many years to convert to days? ")
##days = get_days(years)
##print("You entered ", years, "years.")
##print("That is {} days.".format(days))


# Q14
#def f(x):
#    a=100
#    x+=a
#    return x+a

# Q15
##def f(l,a,b):
##    l.append(a)
##    l=l+[b]
##    return l


# Q17
def f():
    t = 0
    r = int(input('Please input an integer: '))
    while r != 0:
        if r % 2 == 0:
            t += r
        r = int(input('Please input an integer: '))
    return t
    
# Q22
class AnException(Exception):
    pass

def exceptions(l,a):
    l.append(9)
    l.pop(a)
    raise AnException()

# Q23
def rec(x):
    if len(x) == x[0]:
        return x
    return rec(x[2:]+[x[0]])


# Q25
def sum(nums):
    total = 0
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    return (sum(nums[:len(nums)//2])+sum(nums[len(nums)//2:]))


# Q32
class A(object):
    def __init__(self,x):
        self._x = x

    def m1(self,x):
        return self.m2(x)*2

    def m2(self,x):
        return x+1

class B(A):
    def m2(self,y):
        return self._x + y

class C(B):
    def __init__(self,x,y):
        super().__init__(x)
        self._y = y

    def m1(self,x):
        return self.x - self._y

class D(B):
    def __init__(self, x, y):
        super().__init__(x)
        self._x += y
        self._y = y

    def m1(self,y):
        return self._y - y

    def m2(self, x):
        return super().m2(x) + x


a = A(3)
b = B(2)
c = C(2,4)
d = D(1,3)


# Q37
import tkinter as tk
class Screen(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, bg="light blue", width=150, height=150)
        self._x, self._y = (150 / 2, 150 / 2)
        self._redraw()

    def _redraw(self):
        """Redraw the screen after a move."""
        self.delete(tk.ALL)
        ## code block 1 ##
        coords = (self._x - 5, self._y - 5, self._x + 5, self._y + 5)
        self.create_oval(coords, fill="black", width=0)
        
    def _move(self, dx, dy):
        """Move the circle by a given amount."""
        self._x += dx
        self._y += dy
        self._redraw()
        

    def move_left(self):
        self._move(-5, 0)

    def move_right(self):
        self._move(5, 0)


class Controls(tk.Frame):
    BUTTON_WIDTH = 10

    def __init__(self, parent, left, right):
        """ Parameters:
                parent (Tk): Window for widget. left (method): Callback for "left button". right (method): Callback for "right button".
        """
        super().__init__(parent)
        ## code block 2 ##
        leftBtn = tk.Button(self, text="LEFT", width=10, command=left)
        leftBtn.pack(side=tk.LEFT)
        rightBtn = tk.Button(self, text="RIGHT", width=10, command=right)
        rightBtn.pack(side=tk.LEFT)

    
class GameApp(object):
    def __init__(self, master):
        master.title("Game")
        screen = Screen(master)
        controls = Controls(master, screen.move_left, screen.move_right)
        controls.pack(side=tk.LEFT)
        screen.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)



