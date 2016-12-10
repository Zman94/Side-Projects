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

def rotatePoint(centerPoint,point,angle):
    """Rotates a point around another centerPoint. Angle is in degrees.
    Rotation is counter-clockwise"""
    angle = math.radians(angle)
    temp_point = point[0]-centerPoint[0] , point[1]-centerPoint[1]
    temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
    return temp_point

def rotatePolygon(polygon,theta):
    """Rotates the given polygon which consists of corners represented as (x,y), around the ORIGIN, clock-wise, theta degrees"""
    theta = math.radians(theta)
    rotatedPolygon = []
    for corner in polygon:
        rotatedPolygon.append(( corner[0]*math.cos(theta)-corner[1]*math.sin(theta) , corner[0]*math.sin(theta)+corner[1]*math.cos(theta)) )
    return rotatedPolygon

def main():
    MainWindow = terrain()
    MainWindow.terrainLoop()

if __name__ == "__main__":
    # pdb.set_trace()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

