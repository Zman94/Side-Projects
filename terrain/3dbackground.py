from __future__ import print_function
import pygame, sys, time, os
import pdb
from pygame.locals import *
import random
import math
import numpy as np
import noise

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sounds disabled')

scl = 20
cols = 0
rows = 0
w = 1500
h = 1200
translate = -450
centerX = 0
centerY = 0
window_aspect = 0

terrain = [[]]

class terrain(object):
    def __init__(self, width=600, height=600):
        global cols, rows, centerX, centerY, window_aspect, terrain
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))
        cols = w/scl
        rows = h/scl
        centerX = (w)/2
        centerY = (h)/2
        window_aspect = width/height
        for y in range(rows):
            for x in range(cols)
                terrain = [[noise.pnoise2(-10,10,3) for x in range(cols)] for y in range(rows)]

    def terrainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((0,0,0))

            for y in range(rows-1):
                x = 0
                points = list()
                for x in range(cols-1):
                    # points.append((x*scl,y*scl))
                    # points.append((x*scl,(y+1)*scl))
                    tempV = np.dot(rotation_matrix([1,0,0],2*math.pi/3), [x*scl-centerX,-(y*scl-centerY),terrain[y][x]])
                    tempV[0]*=(1.5-(tempV[2]/600))
                    tempV[1]*=(2-(tempV[2]/600))
                    points.append([int(tempV[0]+centerX+translate),int(tempV[1]+centerY)+translate/3])

                    tempV = np.dot(rotation_matrix([1,0,0],2*math.pi/3), [x*scl-centerX,-((y+1)*scl-centerY),terrain[y+1][x]])
                    tempV[0]*=(1.5-(tempV[2]/600))
                    tempV[1]*=(2-(tempV[2]/600))
                    points.append([int(tempV[0]+centerX+translate),int(tempV[1]+centerY)+translate/3])

                    tempV = np.dot(rotation_matrix([1,0,0],2*math.pi/3), [(x+1)*scl-centerX,-(y*scl-centerY),terrain[y][x+1]])
                    tempV[0]*=(1.5-(tempV[2]/600))
                    tempV[1]*=(2-(tempV[2]/600))
                    points.append([int(tempV[0]+centerX+translate),int(tempV[1]+centerY)+translate/3])
                    pygame.draw.lines(self.screen,(255,255,255),True,points,1)
                    points = list()
                # pygame.draw.rect(self.screen,(255,255,255),[0,y*scl,self.width,1],1)
                # pygame.draw.line(self.screen,(255,255,255),rotateX([0,y*scl],self.centerX,self.centerY,.25),rotateX([self.width,y*scl],self.centerX,self.centerY,.25))

            pygame.display.flip()

def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis/math.sqrt(np.dot(axis, axis))
    a = math.cos(theta/2.0)
    b, c, d = -axis*math.sin(theta/2.0)
    aa, bb, cc, dd = a*a, b*b, c*c, d*d
    bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
    return np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
                     [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
                     [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])

def main():
    pygame.init()
    # point(5,5,5)
    MainWindow = terrain()
    MainWindow.terrainLoop()

if __name__ == "__main__":
    # pdb.set_trace()
    main()
    # print("--- %s seconds ---" % (time.time() - start_time))

