###
### Author: Xin Li
### Description:  In this programming assignment,
### In this programming assignment, you will be
### building a program that displays a landscape
### in a graphics canvas and allows the user to
### control the perspective of the landscape by
### moving the mouse. The perspective seems to
### change due to an effect called motion parallax
### , which you should implement in this program.
### The above gif shows an example of the user
### interacting with a completed version of the
### program.
### Name of this program is: motion_parallax.py
from graphics import graphics
import random
def main():
    gui = graphics(600, 600, 'motion_parallax')
    color_string1, color_string2, color_string3 = random_mountian_color(gui)
    x_coord = -600
    x_coord_2 = 0
    x_coord_3 = 0
    while True:
        y_coord = 100
        y_coord_2 = 50
        y_coord_3 = 0
        gui.clear()
        x = gui.mouse_x // 5 + 200
        y = gui.mouse_y // 5 + 200
        blue_canvas(gui, x, y)
        mountains(gui, x, y, color_string1, color_string2, color_string3)
        lake_lawn_and_tree_house(gui, x, y)
        the_birds(gui, x_coord, y_coord)
        x_coord=change_of_x_coord(x_coord)
        the_clouds(gui, x_coord_2, y_coord_2)
        x_coord_2=change_of_x_coord_2(x_coord_2)

        gui.update_frame(60)

def blue_canvas(gui, x, y):
    '''Initially, get a program that generates
    a square canvas, and fill the canvas with
    a blue rectangle. The blue rectangle can serve
    as the sky.
    '''
    gui.rectangle(-10, -10, 620, 620, 'sky blue')
    gui.ellipse(x+150, y-150, 100, 100, 'gold')

def mountains(gui, x, y, color_string1, color_string2, color_string3):
    '''Next, work on getting a static landscape
    displayed. At this point, don鈥檛 worry about
    the motion parallax, random mountain colors,
    or the birds. The shapes will be added the canvas
    in the order you add them programatically.
    '''
    gui.triangle(x+50, y-100, x-150, y+250, x+250, y+250, color_string1)
    gui.triangle(x-150, y-50, x-450, y+250, x+150, y+250, color_string2)
    gui.triangle(x+200, y-50, x-50, y+250, x+550, y+250, color_string3)

def lake_lawn_and_tree_house(gui, x, y):
    gui.rectangle(x-450, y+250, 1000, 300, 'springgreen')
    i = 0
    while i <= 620:
        gui.line(i, y+230, i, y+250, 'springgreen')
        i += 5
    gui.rectangle(x+150, y+230, 20, 50, 'brown')
    gui.ellipse(x+160, y+200, 50, 100, 'green')
    gui.ellipse(x, y+300, 400, 50, 'blue')
    gui.rectangle(x+220, y+250, 100, 100, 'gold4')
    gui.triangle(x+270, y+200, x+220, y+250, x+320, y+250, 'orange')
    gui.rectangle(x+230, y+275, 40, 40, 'sky blue')
    gui.rectangle(x+280, y+275, 30, 60, 'brown')

def random_mountian_color(gui):
    '''Update the program so that it generates three random colors
    for the mountains on each program run.
    '''
    color_string1 = "blue"
    color_string2 = "red"
    color_string3 = "green"
    red =  random.randint(0,255)
    green =  random.randint(0,255)
    blue =  random.randint(0,255)
    color_string1 = gui.get_color_string(blue, red, green)
    color_string2 = gui.get_color_string(red, green, blue)
    color_string3 = gui.get_color_string(green, blue, red)
    return color_string1, color_string2, color_string3


def the_birds (gui, x_coord, y_coord):
    '''add the flying birds to the canvas. You should
    use a while loop. You are not required to make the
    birds move, or to be a part of the parallax.
    '''
    i = 0
    while i < 5:
        gui.line(x_coord+100*i, y_coord+20*i, x_coord+25+100*i, y_coord+10+20*i, 'black', 5)
        gui.line(x_coord+25+100*i, y_coord+10+20*i, x_coord+50+100*i, y_coord+20*i, 'black', 5)
        i += 1
def change_of_x_coord(x_coord):
    x_coord += 10
    if x_coord > 620:
        x_coord = -600
    return x_coord

def the_clouds (gui, x_coord_2, y_coord_2):
    gui.ellipse(x_coord_2, y_coord_2, 150, 50, 'white')
def change_of_x_coord_2(x_coord_2):
    x_coord_2 += 5
    if x_coord_2 > 700:
        x_coord_2 = -200
    return x_coord_2
main()
