from __future__ import print_function
import pygame, sys, time, os
import pdb
import random
import math

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sounds disabled')

class piece:
    def __init__(self, xPos, yPos):
        self.x = xPos
        self.y = yPos

