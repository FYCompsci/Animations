#A line starts in the corner and bounces off of walls
#What will happen when it hits the other corner?
#By Zack Nathan

import sys
import pygame 
from pygame.locals import *
from random import randint, random, choice
from math import *
from time import sleep

pygame.init() 

width = 1200
height = 700

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption ("Bounce off the wall")

#Background
screen.fill((0, 0, 0))

#For fading lines
s = pygame.Surface((width,height))
s.set_alpha(1)

xdir = 5
ydir = 5
x = 0
y = 0
linecolour = (255, 255, 255)

while True:
    
    #Listener
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()

    x += xdir
    y += ydir

    if x >= width and y >= height:
        linecolour = (0, 0, 0)

    if 0 > x or x > width:
        xdir *= -1
    if 0 > y or y > height:
        ydir *= -1

    pygame.draw.circle(screen, linecolour, (x, y), 5, 0)

    print linecolour, x, y

    #Next frame
    pygame.display.flip()

