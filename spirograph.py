#Pygame Spirograph by Zack Nathan
#Created by accident, and uses mechanics from the solar system animation
#Draws cool swirly lines

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
pygame.display.set_caption ("Spirograph by Zack Nathan")

def program():
    global degree

    degree = 0
    frame = 0
    fadetime = 5

    #Choose colour scheme
    bright_on_black = [(0, 0, 0), (0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255)]
    #faded_on_white = [(255, 255, 255), (100, 200, 100), (200, 100, 100), (200, 200, 100), (100, 200, 200), (0, 0, 0)]
    #green_on_grey = [(150, 150, 150), (20, 200, 40), (30, 220, 140), (160, 250, 50), (20, 120, 20), (0, 0, 0)]
    colourschemes = [bright_on_black]
    colourscheme = choice(colourschemes)

    class circle:
        orbitradius = 1
        orbittime = 1
        colour = (255, 255, 255)
        coordinates = [0, 0]

        def render(self):

            global degree

            x = cos(degree * 2 * pi / self.orbittime) * (self.orbitradius + 50)
            y = sin(degree * 2 * pi / self.orbittime) * (self.orbitradius + 50)

            pygame.draw.line(screen, self.colour, (int(self.coordinates[0] + (width/2)), int(self.coordinates[1] + (height/2))), (int(x + (width/2)), int(y + (height/2))), 1)
            
            self.coordinates = [x, y]

    class satellite:
        orbitradius = 1
        orbittime = 1
        colour = (255, 255, 255)
        coordinates = [0, 0]

        def render(self, parent):

            global degree

            x = cos(degree * 2 * pi / self.orbittime) * self.orbitradius
            y = sin(degree * 2 * pi / self.orbittime) * self.orbitradius

            if degree > 2:
                pygame.draw.line(screen, self.colour, ((x + parent.coordinates[0] + (width/2)), (y + parent.coordinates[1] + (height/2))), (int(self.coordinates[0] + (width/2)), int(self.coordinates[1] + (height/2))), 1)
            
            self.coordinates = [x + parent.coordinates[0], y + parent.coordinates[1]]

    #Circle around the center
    a = circle()
    a.orbitradius = randint(height/8, height/4)
    a.orbittime = randint(100, 500)
    if random() > 0.5:
        a.orbittime *= -1
    a.colour = (100, 100, 100)

    #Moves around a
    b = satellite()
    b.orbitradius = randint(10, height/12)
    b.orbittime = randint(20, 100)
    if random() > 0.5:
        b.orbittime *= -1
    b.colour = colourscheme[1]

    #Moves around b
    c = satellite()
    c.orbitradius = randint(10, height/12)
    c.orbittime = randint(20, 100)
    if random() > 0.5:
        c.orbittime *= -1
    c.colour = colourscheme[2]

    #Moves around c
    d = satellite()
    d.orbitradius = randint(10, height/12)
    d.orbittime = randint(20, 100)
    if random() > 0.5:
        d.orbittime *= -1
    d.colour = colourscheme[3]

    #Moves around d
    e = satellite()
    e.orbitradius = randint(10, height/12)
    e.orbittime = randint(20, 100)
    if random() > 0.5:
        e.orbittime *= -1
    e.colour = colourscheme[4]

    #Moves around e
    f = satellite()
    f.orbitradius = randint(10, height/12)
    f.orbittime = randint(20, 100)
    if random() > 0.5:
        f.orbittime *= -1
    f.colour = colourscheme[5]

    #Moves around f
    g = satellite()
    g.orbitradius = randint(10, height/12)
    g.orbittime = randint(20, 100)
    if random() > 0.5:
        g.orbittime *= -1
    g.colour = colourscheme[6]

    #Background
    screen.fill(colourscheme[0])

    #For fading lines
    s = pygame.Surface((width,height))
    s.set_alpha(1)

    while True:
        
        #Listener
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                if event.key == K_RETURN:
                    program()
                if event.key == K_UP:
                    a.orbittime -= a.orbittime*0.1
                    b.orbittime -= b.orbittime*0.1
                    c.orbittime -= c.orbittime*0.1
                    d.orbittime -= d.orbittime*0.1
                    e.orbittime -= e.orbittime*0.1
                    f.orbittime -= f.orbittime*0.1
                    g.orbittime -= g.orbittime*0.1
                    degree -= degree*0.1
                    fadetime -= fadetime*0.1
                if event.key == K_DOWN:
                    a.orbittime += a.orbittime*0.1
                    b.orbittime += b.orbittime*0.1
                    c.orbittime += c.orbittime*0.1
                    d.orbittime += d.orbittime*0.1
                    e.orbittime += e.orbittime*0.1
                    f.orbittime += f.orbittime*0.1
                    g.orbittime += g.orbittime*0.1
                    degree += degree*0.1
                    fadetime += fadetime*0.1

        degree += 1
        frame += 1

        #Draw the lines
        a.render()
        b.render(a)
        c.render(b)
        d.render(c)
        e.render(d)
        f.render(e)
        g.render(f)

        #Fading lines
        if frame % fadetime < 1:
            s.fill(colourscheme[0])
            screen.blit(s, (0,0))

        #Point in the center
        pygame.draw.circle(screen, colourscheme[7], (width/2, height/2), 5, 0)

        #Next frame
        pygame.display.flip()

program()

