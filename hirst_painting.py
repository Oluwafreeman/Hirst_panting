from turtle import Turtle, Screen

timmy = Turtle()
# Turtle.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return(r, g, b)

# timmy.shape("turtle")
# timmy.color("coral")
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# def draw_shape(side):
#     angle = 360//side
#     for size in range(side):
#         timmy.forward(50)
#         timmy.right(angle)

# for num in range(3, 11):
#     draw_shape(num)

# import random
# direction = [90, 180, 270,360]
# timmy.pensize(5)
# timmy.color(random_color())


# for i in range(50):
#     timmy.speed("fast")
#     timmy.forward(10)
#     timmy.setheading(random.choice(direction))


# timmy.speed("fastest")
# def draw_spirograph(size_of_gap):

#     for _ in range(int(360/size_of_gap)):
#         timmy.circle(50)
#         timmy.setheading(timmy.heading() 
#         + size_of_gap)

# draw_spirograph(17)

# import colorgram

# colors = colorgram.extract("image.jpg", 30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 
121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    timmy.dot(20)
    timmy.forward(50) 

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = Screen()
screen.exitonclick()