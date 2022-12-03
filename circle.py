import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r,g,b)
    return colour

t.forward(100)
t.setheading(90)
t.forward(100)

screen = t.Screen()
screen.exitonclick()