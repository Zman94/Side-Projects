from __future__ import print_function
import pygame, sys, time, os
import pdb
from pygame.locals import *
import random
import math

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sounds disabled')

scl = 20
cols = 0
rows = 0
centerX = 0
centerY = 0
window_aspect = 0

class terrain(object):
    def __init__(self, width=600, height=600):
        global cols, rows, centerX, centerY, window_aspect
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))
        centerX = width/2
        centerY = height/2
        cols = width/scl
        rows = height/scl
        window_aspect = width/height

    def terrainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((0,0,0))

            for y in range(rows+1):
                points = list()
                for x in range(cols+1):
                    # points.append((x*scl,y*scl))
                    # points.append((x*scl,(y+1)*scl))
                    points.append(rotateX(x*scl,y*scl,math.pi/4))
                    points.append(rotateX(x*scl,(y+1)*scl,math.pi/4))
                # pygame.draw.rect(self.screen,(255,255,255),[0,y*scl,self.width,1],1)
                pygame.draw.lines(self.screen,(255,255,255),False,points,1)
                points = [rotateX(0,y*scl,math.pi/4),rotateX(self.width,y*scl,math.pi/4),rotateX(self.width,y*scl+1,math.pi/4),rotateX(0,y*scl+1,math.pi/4)]
                pygame.draw.lines(self.screen,(255,255,255),True,points,1)
                # pygame.draw.line(self.screen,(255,255,255),rotateX([0,y*scl],self.centerX,self.centerY,.25),rotateX([self.width,y*scl],self.centerX,self.centerY,.25))

            pygame.display.flip()

def rotateX(x,y,radians):
    # origX = x
    origY = y
    y = y-centerY
    x = x-centerX
    d = y
    theta = radians
    y = centerY + d * math.cos(theta)
    xChange = int(((1-((y/centerY)*math.sin(theta))/.5))*x)
    x+=(centerX-xChange)
    # x = origX
    # y = origY
    return (x,y)

def main():
    pygame.init()
    # point(5,5,5)
    MainWindow = terrain()
    MainWindow.terrainLoop()

if __name__ == "__main__":
    # pdb.set_trace()
    main()
    # print("--- %s seconds ---" % (time.time() - start_time))

