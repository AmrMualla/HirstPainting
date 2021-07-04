#AmrMualla Hirst Painting Vibrant Mona Lisa Combo ;)
import colorgram
from os.path import dirname, join
import turtle as t
import random
current_dir = dirname(__file__)
file_path = join(current_dir, "./image.jpg")

rgb_colors = []
colors = colorgram.extract(file_path, 30)
for color in colors:
    rgb_colors.append(color.rgb)

t.colormode(255)
timur = t.Turtle()
timur.hideturtle()
timur.speed(0)
color_list = [( 234,  225,  81),  ( 158,  84,  32), ( 244,  238,  194), ( 211,  160,  87), ( 41,  100,  161), ( 194,  158,  22), ( 94,  173,  221), ( 15,  30,  64), ( 64,  26,  10), ( 198,  229,  247), ( 211,  246,  228), ( 61,  16,  38), ( 138,  66,  101), ( 143,  20,  58), ( 28,  49,  135), ( 147,  28,  12), ( 247,  230,  242), ( 114,  237,  170), ( 118,  191,  140), ( 221,  223,  6), ( 75,  113,  207), ( 193,  136,  165), ( 15,  34,  21), 
( 16,  173,  221), ( 201,  78,  121), ( 63,  116,  78), ( 218,  85,  56), ( 110,  225,  245), ( 52,  190,  93), ( 95,  80,  12)]

timur.setheading(225)
timur.penup()
timur.forward(300)
timur.setheading(0)
timur.pendown()
dot_number = 101

for count in range(1, dot_number):
    timur.dot(20, random.choice(color_list))
    timur.penup()
    timur.forward(50)
    timur.pendown()

    if count % 10 == 0:
        timur.setheading(90)
        timur.penup()
        timur.forward(50)
        timur.setheading(180)
        timur.penup()
        timur.forward(500)
        timur.setheading(0)
        timur.pendown()

screen = t.Screen()
screen.exitonclick()


