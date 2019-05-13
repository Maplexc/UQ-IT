import turtle

def demo():
    """turtle demo."""
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(80)
    turtle.exitonclick()


def rectangle(width,height):
    """draws a rectangle with the given side lengths
    Parameter:
        width(int): width of rectangle
        height(int): height of rectangle
    """
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)

#if __name__ == "__main__":
#    rectangle(90,50)
#    turtle.exitonclick


def rotated_rectangle(width,height,angle):
    """draw a rectangle rotated anticlockwise by the given angle
    Parameter:
        width(int): width of rectangle
        height(int): height of rectangle
        angle(int):angle that rotated rectangle anticlockwise
    """
    turtle.left(angle)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90-angle)
    turtle.exitonclick()

def rotated_rectangle1(width,height,angle):
    turtle.left(angle)
    for i in range(0,3):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
    turtle.left(-angle)
    turtle.exitonclick()

def rotated_rectangle2(width,height,angle):
    turtle.left(angle)
    for i in range(0,4):
        if i%2 ==0:
            turtle.forward(width)
        else:
            turtle.forward(height)
        turtle.left(90)
    turtle.exitonclick()

def rotated_rectangle_ans(width,height,angle):
    turtle.left(angle)
    rectangle(width,height)

def polygon(radius, num_sides):
    """draw a regular polygon with n sides
    Parameters:
        radius (int):radius of polygon
        num_sides (int): number of sides of the polygon
    """
    import math
    side_length=radius*math.sin(math.pi/num_sides)
    for i in range(0,num_sides):
        turtle.forward(side_length)
        turtle.left(360/num_sides)
    turtle.exitonclick()

def interact():
    """interact with user: first asks the user for a distance, then repeatedly asks for a direction to move, from the options n/s/e/w
    """
    distance=int(input('plz enter a distence:'))
    direction=''
    while direction!='p':
        direction=input('plz enter a direction (from n/s/e/w):')    
        if direction=='n':
            turtle.left(90)
            turtle.forward(distance)
            turtle.left(-90)
        elif direction=='s':
            turtle.right(90)
            turtle.forward(distance)
            turtle.right(-90)
        elif direction=='e':
            turtle.forward(distance)
        elif direction=='w':
            turtle.backward(distance)
        if direction=='p':
            turtle.exitonclick()
        else:
            print('that''s not a direction')
        

def spiral(num_lines, step_size):
    """draws a square spiral with num_lines lines, which starting from the centre have length s, s, 2s, 2s
    Parameters:
        num_lines (int):number of line
        step_size (int):size of each line
    """
    num_step=0
    times=2
    s=step_size
    while num_step<=num_lines:
        turtle.forward(s)
        turtle.left(90)
        num_step+=1
        if num_step<=num_lines:
            turtle.forward(s)
            turtle.left(90)
            num_step+=1
        s=times*step_size
        times+=1
    turtle.exitonclick()
    




