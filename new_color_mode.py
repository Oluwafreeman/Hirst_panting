import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r, g, b)


direction = [90, 180, 270,360]
for i in range(50):
    tim.width(5)
    tim.color(random_color())
    tim.speed("fast")
    tim.forward(10)
    tim.setheading(random.choice(direction))


# print(random_color())
my_screen = t.Screen()
my_screen.exitonclick()