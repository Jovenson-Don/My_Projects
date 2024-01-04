###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random

paint = t
paint.penup()
screen = t.Screen()
paint.speed("fastest")
paint.setx(-250)
paint.sety(-250)
paint.hideturtle()


y = -250

paint.colormode(255)
color_list = [(149, 50, 75), (222, 136, 201), (53, 123, 93), (170, 41, 154), (138, 20, 31), (134, 184, 163), (197, 73, 92), (47, 86, 121), (73, 35, 43), (145, 149, 178), (14, 70, 98), (232, 165, 176), (160, 158, 142), (54, 50, 45), (101, 77, 75), (183, 171, 205), (36, 74, 60), (19, 89, 86), (82, 129, 148), (147, 19, 17), (27, 102, 68), (12, 64, 70), (107, 153, 127), (176, 208, 192), (168, 102, 99)]


def paint_dot_in_straight_line():
    for _ in range(10):
        paint.dot(20, random.choice(color_list))
        paint.forward(50)
    paint.goto(0, y + 50)
    return 50


def change_y_axis():
    paint.goto(-250, y + 50)
    return 50


for _ in range(10):
    paint_dot_in_straight_line()
    y += change_y_axis()


screen.exitonclick()
