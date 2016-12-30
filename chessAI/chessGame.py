from __future__ import print_function
import pygame, sys, time, os
import pdb
import random
import math

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sounds disabled')

class piece(object):
    def __init__(self, xPos, yPos, movement, fullBoard=True, pawn=False):
        self.x = xPos
        self.y = yPos
        self.moves = movement
        self.fullBoard = fullBoard
        self.pawn = pawn
        self.home = True

class pawn(piece):
    def __init__(self, xPos, yPos):
        piece.__init__(self, xPos, yPos, ["y1","y2","y1x1c"], False, True)

class knight(piece):
    def __init__(self, xPos, yPos):
        piece.__init__(self, xPos, yPos, ["y1x2","y2x1"], False)

class bishop(piece):
    def __init__(self, xPos, yPos):
        piece.__init__(self, xPos, yPos, ["y1x1"])

class rook(piece):
    def __init__(self, xPos, yPos):
        piece.__init__(self, xPos, yPos, ["y1","x1"])

class queen(piece):
    def __init__(self, xPos, yPos):
        piece.__init__(self, xPos, yPos, ["y1","x1","y1x1"])

class king(piece):
    def __init__(self, xPos, yPos):
        piece.__init__(self, xPos, yPos, ["y1","x1","y1x1"], False)
