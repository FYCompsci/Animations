#Pygame Solar System by Zack Nathan
#Draws the sun, planets, the moon, asteroid belt, and background stars
#The planets and asteroids orbit around the sun

import sys
import pygame 
from pygame.locals import *
from random import randint
from math import *
from time import sleep

pygame.init() 

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption ("Solar System Simulation")

x = 600
y = 400
degree = 0

class planet:
    size = 1
    orbitradius = 1
    orbittime = 1
    colour = (255, 255, 255)
    ringcolour = (0, 0, 0)
    rings = False
    dot = False
    coordinates = [0, 0]

    def render(self):

        global degree

        x = cos(degree * 2 * pi / self.orbittime) * (self.orbitradius + 50)
        y = sin(degree * 2 * pi / self.orbittime) * (self.orbitradius + 50)
        self.coordinates = [x, y]
        pygame.draw.circle(screen, self.colour, (int(x + 600), int(y + 400)), int(self.size/2), 0)

        if self.rings == True:
            pygame.draw.circle(screen, self.ringcolour, (int(x + 600), int(y + 400)), int(self.size), 0)
            pygame.draw.circle(screen, (0, 0, 0), (int(x + 600), int(y + 400)), int(self.size/1.5), 0)
            pygame.draw.circle(screen, self.colour, (int(x + 600), int(y + 400)), int(self.size/2), 0)

        if self.dot == True:
            pygame.draw.circle(screen, self.dotcolour, (int(x + 600 - 7), int(y + 400 + 7)), 3, 0)

class moon:
    size = 1
    orbitradius = 1
    orbittime = 1
    colour = (255, 255, 255)
    coordinates = [0, 0]

    def render(self, planet):

        global degree

        x = cos(degree * 2 * pi / self.orbittime) * self.orbitradius
        y = sin(degree * 2 * pi / self.orbittime) * self.orbitradius
        self.coordinates = [x + planet.coordinates[0], y + planet.coordinates[1]]
        pygame.draw.circle(screen, self.colour, (int(x + 600 + planet.coordinates[0]), int(y + 400 + planet.coordinates[1])), int(self.size/2), 0)

#Solar System
mercury = planet()
mercury.size = 4.879
mercury.orbitradius = 30
mercury.orbittime = 88
mercury.colour = (138, 123, 76)

venus = planet()
venus.size = 12.104
venus.orbitradius = 70
venus.orbittime = 225
venus.colour = (247, 225, 136)

earth = planet()
earth.size = 12.756
earth.orbitradius = 110
earth.orbittime = 365
earth.colour = (20, 200, 200)

earthmoon = moon()
moon.size = 4
moon.orbitradius = 12
moon.orbittime = 30
moon.colour = (150, 150, 150)
moon.planet = earth

mars = planet()
mars.size = 6.792
mars.orbitradius = 150
mars.orbittime = 500
mars.colour = (209, 49, 0)

jupiter = planet()
jupiter.size = 40
jupiter.orbitradius = 250
jupiter.orbittime = 1100
jupiter.colour = (255, 196, 133)
jupiter.dot = True
jupiter.dotcolour = (191, 54, 0)

saturn = planet()
saturn.size = 32
saturn.orbitradius = 350
saturn.orbittime = 1500
saturn.colour = (232, 207, 132)
saturn.rings = True
saturn.ringcolour = (156, 118, 8)

uranus = planet()
uranus.size = 24
uranus.orbitradius = 450
uranus.orbittime = 1800
uranus.colour = (144, 184, 240)

neptune = planet()
neptune.size = 22
neptune.orbitradius = 550
neptune.orbittime = 2200
neptune.colour = (27, 19, 240)

starsx = []
starsy = []
for i in range(100):
    starsx.append(randint(0, 1200))
    starsy.append(randint(0, 800))

asteroidbelt = []
for i in range(100):
    asteroidbelt.append([randint(190, 210), randint(600, 1000)])

def asteroidbeltrender():
    global degree

    for i in range(100):
        x = cos((degree + 7 * i) * 2 * pi / asteroidbelt[i][1]) * (asteroidbelt[i][0] + 50)
        y = sin((degree + 7 * i) * 2 * pi / asteroidbelt[i][1]) * (asteroidbelt[i][0] + 50)
        pygame.draw.circle(screen, (100, 100, 100), (int(x + 600), int(y + 400)), 1, 0)


while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   sys.exit()

    degree += 2
    screen.fill((0, 0, 0))
    sleep(0.01)

    for i in range(100):
        pygame.draw.circle(screen, (255, 255, 255), (starsx[i], starsy[i]), 1, 0)

        mercury.render()
        venus.render()

        earth.render()
        earthmoon.render(earth)

        mars.render()
        asteroidbeltrender()
        jupiter.render()
        saturn.render()
        uranus.render()
        neptune.render()

    pygame.draw.circle(screen, (255, 180, 20), (600, 400), 50, 0)

    pygame.display.flip()

