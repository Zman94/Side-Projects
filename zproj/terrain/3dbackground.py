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
w = 600
h = 1200
translateX = -70
translateY = -400
centerX = 0
centerY = 0
window_aspect = 0
flying = 0

terrainz = list()

class terrain(object):
    def __init__(self, width=400, height=400):
        global cols, rows, centerX, centerY, window_aspect, terrainz
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))
        cols = w/scl
        rows = h/scl
        centerX = (w)/2
        centerY = (h)/2
        window_aspect = width/height

    def terrainLoop(self):
        global flying
        xoff, yoff = 0,0
        for y in range(rows):
            terrainz.append(list())
            for x in range(cols):
                terrainz[y].append(noise.pnoise2(xoff,yoff))

        while True:
            flying-=.15
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((0,0,0))

            yoff = flying
            for y in range(rows):
                xoff = 0
                for x in range(cols):
                    terrainz[y][x]=35*noise.pnoise2(xoff,yoff)
                    xoff+=.15
                yoff+=.15

            for y in range(rows-1):
                x = 0
                points = list()
                for x in range(cols-1):
                    tempV = np.dot(rotation_matrix([1,0,0],1.8*math.pi/3), [x*scl-centerX,-(y*scl-centerY),terrainz[y][x]])
                    tempV[0]*=(1.5-(tempV[2]/600))
                    tempV[1]*=(2-(tempV[2]/600))
                    points.append([int(tempV[0]+centerX+translateX),int(tempV[1]+centerY)+translateY/2])

                    tempV = np.dot(rotation_matrix([1,0,0],1.8*math.pi/3), [x*scl-centerX,-((y+1)*scl-centerY),terrainz[y+1][x]])
                    tempV[0]*=(1.5-(tempV[2]/600))
                    tempV[1]*=(2-(tempV[2]/600))
                    points.append([int(tempV[0]+centerX+translateX),int(tempV[1]+centerY)+translateY/2])

                    tempV = np.dot(rotation_matrix([1,0,0],1.8*math.pi/3), [(x+1)*scl-centerX,-(y*scl-centerY),terrainz[y][x+1]])
                    tempV[0]*=(1.5-(tempV[2]/600))
                    tempV[1]*=(2-(tempV[2]/600))
                    points.append([int(tempV[0]+centerX+translateX),int(tempV[1]+centerY)+translateY/2])
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

