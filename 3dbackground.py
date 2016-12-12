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

class terrain:
    def __init__(self, width=600, height=600):
        global cols, rows
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))
        cols = width/scl
        rows = height/scl

    def terrainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0,0,0))

            for y in range(rows):
                points = list()
                for x in range(cols):
                    points.append(rotatePoint([x*scl,self.height/2],[x*scl,y*scl],5))
                    points.append(rotatePoint([x*scl,self.height/2],[x*scl,(y+1)*scl],5))
                    # pygame.draw.rect(self.screen,(255,255,255),[x*scl,y*scl,scl,scl],1)
                pygame.draw.lines(self.screen,(255,255,255),False,points,2)
                pygame.draw.line(self.screen,(255,255,255),[0,y*scl],[self.width,y*scl])

            pygame.display.flip()

def main():
    MainWindow = terrain()
    MainWindow.terrainLoop()

if __name__ == "__main__":
    # pdb.set_trace()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

