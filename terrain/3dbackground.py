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

class pointNode(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def rotateX(self,rad):
        # return xy
        x = self.x-centerX
        y = self.y-centerY
        self.y = (y*math.cos(rad)-self.z*math.sin(rad))+centerY
        self.z = y*math.sin(rad)+self.z*math.cos(rad)
        return
        final = list()
        x = self.x-centerX
        y = self.y-centerY
        z = self.z

        d = math.hypot(y,z)
        theta = math.atan2(y,z)+radians
        self.y = centerY+d*math.sin(theta)
        self.z = d*math.cos(theta)

    def project(self, fov=256, viewer_distance=4):
        factor = fov/(viewer_distance+self.z)
        x = self.x*factor+centerX
        y = -self.y*factor+centerY
        return [x,y]

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
            points3d = list()
            points3d.append(pointNode(50,50,0))
            points3d.append(pointNode(100,50,0))
            points3d.append(pointNode(100,100,0))
            points3d.append(pointNode(50,100,0))

            # for point in points3d:
            #     point.rotateX(0)

            points = list()
            for point in points3d:
                points.append(point.project())

            # for y in range(rows):
            #     points = list()
            #     for x in range(cols):
            #         points.append(rotateX([x*scl,y*scl],self.centerX, self.centerY,.25))
            #         points.append(rotateX([x*scl,(y+1)*scl],self.centerX,self.centerY,.25))
                    # pygame.draw.rect(self.screen,(255,255,255),[x*scl,y*scl,scl,scl],1)
            pygame.draw.lines(self.screen,(255,255,255),True,points,2)
                # pygame.draw.line(self.screen,(255,255,255),rotateX([0,y*scl],self.centerX,self.centerY,.25),rotateX([self.width,y*scl],self.centerX,self.centerY,.25))

            pygame.display.flip()

def main():
    pygame.init()
    # point(5,5,5)
    MainWindow = terrain()
    MainWindow.terrainLoop()

if __name__ == "__main__":
    # pdb.set_trace()
    main()
    # print("--- %s seconds ---" % (time.time() - start_time))

