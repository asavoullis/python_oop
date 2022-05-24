import turtle
import matplotlib.pyplot as plt
import time
import math

"""https://www.youtube.com/watch?v=tmY6FEF8f1o"""


class Polygon:
    """ Triangles Squares Pentagons Hexagons etc """
    # constructor __init__ of class runs every time we make a new object
    def __init__(self, sides, name, side_length=100, colour="black", line_thickness=5, x_pos=90, y_pos=90):
        # we added a default value to the parameters side_length and color
        """ always when using init the first parameter we pass is self
        and then we need to think what else is important to our class.

        In this case we need to think what is important to a polygon.
        For example sides, and maybe we need to give it a name too.
        """
        # The last step when initialising things is to define the parameters
        # properties
        self.sides = sides
        self.name = name
        self.side_length = side_length
        self.colour = colour
        self.line_thickness = line_thickness

        self.x_pos = x_pos
        self.y_pos = y_pos

        # now we have defined 2 more properties of our class which are not parameters
        # these are computed on initialisation - depending on the number of sides we pass in

        # the general formula for any polygon is (n-2) x 180
        # for specific angles the formula is ( (n-2) x 180 ) / n
        self.sum_interior_angles = (self.sides - 2) * 180
        self.individual_angle = self.sum_interior_angles / self.sides

    # define a method - because this is a class method first we need to pass in self
    # we can access sides and name by passing self
    def draw(self):
        # stop writing - lift the pen up
        turtle.penup()
        # go to this position -
        turtle.setpos(self.x_pos, self.y_pos)
        for i in range(self.sides):
            # start writing
            turtle.pendown()
            turtle.color(self.colour)
            turtle.pensize(self.line_thickness)
            turtle.forward(self.side_length)
            # we can use the self parameter that we have passed into our class method to access the self.individual_angle
            # that we initialised on the creation of our class to turn x degrees
            turtle.right(180 - self.individual_angle)

        # done and mainloop are the same thing
        # turtle.done()
        # turtle.mainloop()


# concept of inheritance and subclassing
# parent class and child class
class Square(Polygon):
    """
    Square is a child class of Polygon, the parent class is Polygon
    Square is utilising polygon
    """

    def __init__(self, side_length=100, colour="black", line_thickness=5, x_pos=90, y_pos=90):
        """
        We don't have to pass all the parameters of the parent class
        Because a square has 4 sides and its name is square and its angles are 90 degrees
        We just need to pass the other parameters of the drawing settings

        Subclassing allows us to reuse code instead of having to rewriting code
        """
        # To specify the size, name and angles we can use the super method
        # This means take from the Polygon parent class
        super().__init__(4, "Square", side_length, colour, line_thickness, x_pos, y_pos)
        # if you set one of the above parameters = to something or just something then they will be always like that
        # for example if we set colour="black" it will always be black same as 4, which is the size

    def draw(self):
        """ Overwriting and extending the draw method - inherited from Polygon class """
        turtle.fillcolor(self.colour)
        turtle.begin_fill()
        # same thing as super - Polygon.draw()
        super().draw()
        turtle.end_fill()


class Point:
    """ Defining a point class
    a 2 dimensional point
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self):
        fig = plt.scatter(self.x, self.y)

    def __add__(self, other):
        """ the other is a point type """
        if isinstance(other, Point):
            # this case is to add Points together
            x = self.x + other.x
            y = self.y + other.y
            return Point(x, y)
        else:
            # this case is to add just numbers eg a + 5
            x = self.x + other
            y = self.y + other
            return Point(x, y)


class Shape:
    """ """

    def __init__(self, sides, name, angle1, angle2, colour, side_length=100, line_thickness=5, x_pos=90, y_pos=90):
        # we added a default value to the parameters side_length and color
        """ always when using init the first parameter we pass is self
        and then we need to think what else is important to our class.

        In this case we need to think what is important to a polygon.
        For example sides and maybe we need to give it a name too.
        """
        # The last step when initialising things is to define the parameters
        # properties
        self.sides = sides
        self.name = name
        self.side_length = side_length
        self.colour = colour
        self.line_thickness = line_thickness

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.angle1 = angle1
        self.angle2 = angle2

    def drawStar(self):
        turtle.clearscreen()
        turtle.pencolor(self.colour)
        turtle.fillcolor('yellow')
        turtle.begin_fill()
        # stop writing - lift the pen up
        turtle.penup()
        # go to this position -
        turtle.setpos(self.x_pos, self.y_pos)
        # set the speed that turtle draws
        turtle.speed(20)

        for i in range(self.sides):
            # start writing
            turtle.pendown()
            turtle.pensize(self.line_thickness)
            turtle.forward(self.angle1)
            turtle.left(self.angle2)

        turtle.end_fill()
        # turtle.done()


def main():
    """ Shape - Star """

    star = Shape(50, 'Star', angle1=200, angle2=170, line_thickness=1, x_pos=-100, y_pos=0, colour='red')
    star.drawStar()
    time.sleep(1)
    # Delete all drawings and all turtles from the TurtleScreen. Reset the now empty TurtleScreen to its initial state:
    # white background, no background image, no event bindings and tracing on.
    turtle.clearscreen()

    """ Point """

    a = Point(1, 1)
    b = Point(2, 2)
    print("Point b:", b.x)

    # concept of overloading - we can overwrite the default process that + does for the Point Class
    # so that we can make it know how to add a + b even though it's not a python built in type
    c = a + b
    print("Point c:", c.x, c.y)

    e = Point(0, 2)
    d = e + 5
    f = a + Point(1, 1)

    print("d.x:", d.x, '\n')

    listAZ = [a, b, c, d, e, f]

    for i in listAZ:
        i.plot()

    plt.show()

    """ Polygons """

    # By feeding in these parameters 4 and squares we have created a Polygon class
    # The only thing we need to initialise the polygon object are the parameters after the self - sides and name
    square = Polygon(4, "Square", 100, line_thickness=10, x_pos=-300, y_pos=-20)
    pentagon = Polygon(5, "Pentagon", colour="red", x_pos=-50, y_pos=-220)
    hexagon = Polygon(6, "Hexagon", 150, "orange", x_pos=180, y_pos=320)

    print(square.name, ':')
    print(square.sides)
    print(square.sum_interior_angles)
    print(square.individual_angle, '\n')
    turtle.clearscreen()
    square.draw()
    time.sleep(1)

    # draw_function(5, 20, 108, 4, "red")
    turtle.clearscreen()
    hexagon.draw()

    print(pentagon.name, ':')
    print(pentagon.sides, '\n')
    turtle.clearscreen()
    pentagon.draw()
    time.sleep(1)

    # Subclassing
    # we can even pass it arguments
    square2 = Square(colour="red", side_length=250, x_pos=92, y_pos=-100)
    print("square2_subclassing:", square2.sides)
    print(square2.individual_angle, '\n')
    turtle.clearscreen()
    square2.draw()

    # this leaves the screen open when done drawing -
    # if you try to draw something below this it will not be drawn it will pause of the last one, above
    turtle.done()
    # turtle.mainloop()


if __name__ == '__main__':
    main()


def draw_function(sides, side_length, individual_angle, line_thickness, colour, x_pos, y_pos):
    """ How the function would look without classes """
    # stop writing - lift the pen up
    turtle.penup()
    turtle.setpos(y_pos, x_pos)
    for i in range(sides):
        # start writing
        turtle.pendown()

        turtle.color(colour)
        turtle.pensize(line_thickness)
        # moves x pixels forward
        turtle.forward(side_length)
        # we can use the self parameter that we have passed into our class method to access the self.individual_angle
        # that we initialised on the creation of our class to turn x degrees
        turtle.right(180 - individual_angle)

    turtle.pendown()
    turtle.done()
