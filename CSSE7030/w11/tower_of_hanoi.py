# split the tower on from_pole to bottom disk and top tower
# first step: move top tower to other_pole
# second step: move bottom disk to to_pole
# third step: move top tower to to_pole
# recursion

# tower of hanoi
def towers(from_pole, to_pole, other_pole, n):
    """ Print out instructions for moving a tower of n disks
        from the from_ slot to the to_ slot.
        d is not really required"""
    if n == 0:
        return
    else:
        towers(from_pole,other_pole, to_pole, n-1)
        print("move disc from {0} to {1}".format(from_pole, to_pole))
        towers(other_pole, to_pole, from_pole, n-1)
        
              
import turtle
def eg():
    turtle.reset()
    turtle.up()
    turtle.goto(-200,-150)
    turtle.down()
    # turtle.speed('fastest')
    turtle.begin_fill()
    turtle.color('blue')
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.end_fill()

def koch(depth,size):
    turtle.reset()
    turtle.up()
    turtle.goto(-200,-150)
    turtle.down()
    koch_edge(depth, size)
    turtle.left(120)
    koch_edge(depth, size)
    turtle.left(120)
    koch_edge(depth, size)

def koch_edge_0(size):
    """ generate the basic shape"""
    turtle.forward(size/3)
    turtle.right(60)
    turtle.forward(size/3)
    turtle.left(120)
    turtle.forward(size/3)
    turtle.right(60)
    turtle.forward(size/3)

def koch_edge_1(size):
    koch_edge_0(size/3)
    turtle.right(60)
    koch_edge_0(size/3)
    turtle.left(120)
    koch_edge_0(size/3)
    turtle.right(60)
    koch_edge_0(size/3)






