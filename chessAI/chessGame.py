from __future__ import print_function
import pygame
import sys
# import time
# import os
# import pdb
# import random
# import math

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sounds disabled')

WIDTH = 600
HEIGHT = 600
BOARDSIZE = 8

BKG, BQG, BRG, BBG, BNG, BPG = None, None, None, None, None, None
WKG, WQG, WRG, WBG, WNG, WPG = None, None, None, None, None, None
DOTG = None

# BKrect, BQrect, BRrect, BBrect, BNrect, BPrect=None, None, None, None, None, None
# WKrect, WQrect, WRrect, WBrect, WNrect, WPrect=None, None, None, None, None, None

BLACKPIECES, WHITEPIECES = list(), list()

class Piece(object):
    def __init__(self, xPos, yPos, graphic, movement, fullBoard=True, isPawn=False):
        self.x = xPos
        self.y = yPos
        self.moves = movement
        self.fullBoard = fullBoard
        self.isPawn = pawn
        self.start = True
        self.graphic = graphic
        self.enabled = False
        self.posMoves = list()

    def getMoves(self, screen, blackSquaresOc, whiteSquaresOc):
        ############ Black ############
        if not whiteTurn:
            if BLACKPIECES[piece].enabled:
                BLACKPIECES[piece].posMoves = list()
                for move in BLACKPIECES[piece].moves:
                    move_x = int(move[0])
                    move_y = int(move[1])
                    move_mod = move[2]
                    move_x_temp = move_x
                    move_y_temp = move_y
                    if blackpiece[piece].pawn == False:
                        if blackpiece[piece].fullBoard:
                            while BLACKPIECES[piece].x-move_x_temp >= 0 and BLACKPIECES[piece].y-move_y_temp >= 0:
                                if (BLACKPIECES[piece].x-move_x_temp, BLACKPIECES[piece].y-move_y_temp) in blackSquaresOc:
                                    break
                                screen.blit(DOTG, ((BLACKPIECES[piece].x-move_x_temp)*WIDTH/BOARDSIZE, (BLACKPIECES[piece].y-move_y_temp)*HEIGHT/BOARDSIZE))
                                BLACKPIECES[piece].posMoves.append((BLACKPIECES[piece].x-move_x_temp, BLACKPIECES[piece].y-move_y_temp))
                                if (BLACKPIECES[piece].x-move_x_temp, BLACKPIECES[piece].y-move_y_temp) in whiteSquaresOc:
                                    break
                                move_x_temp+=move_x
                                move_y_temp+=move_y
                                move_x_temp = move_x
                                move_y_temp = move_y
                            while BLACKPIECES[piece].x-move_x_temp >= 0 and BLACKPIECES[piece].y+move_y_temp < 8:
                                if (BLACKPIECES[piece].x-move_x_temp, BLACKPIECES[piece].y+move_y_temp) in blackSquaresOc:
                                    break
                                screen.blit(DOTG, ((BLACKPIECES[piece].x-move_x_temp)*WIDTH/BOARDSIZE, (BLACKPIECES[piece].y+move_y_temp)*HEIGHT/BOARDSIZE))
                                BLACKPIECES[piece].posMoves.append((BLACKPIECES[piece].x-move_x_temp, BLACKPIECES[piece].y+move_y_temp))
                                if (BLACKPIECES[piece].x-move_x_temp, BLACKPIECES[piece].y+move_y_temp) in whiteSquaresOc:
                                    break
                                move_x_temp+=move_x
                                move_y_temp+=move_y
                                move_x_temp = move_x
                                move_y_temp = move_y
                            while BLACKPIECES[piece].x+move_x_temp < 8 and BLACKPIECES[piece].y-move_y_temp >= 0:
                                if (BLACKPIECES[piece].x+move_x_temp, BLACKPIECES[piece].y-move_y_temp) in blackSquaresOc:
                                    break
                                screen.blit(DOTG, ((BLACKPIECES[piece].x+move_x_temp)*WIDTH/BOARDSIZE, (BLACKPIECES[piece].y-move_y_temp)*HEIGHT/BOARDSIZE))
                                BLACKPIECES[piece].posMoves.append((BLACKPIECES[piece].x+move_x_temp, BLACKPIECES[piece].y-move_y_temp))
                                if (BLACKPIECES[piece].x+move_x_temp, BLACKPIECES[piece].y-move_y_temp) in whiteSquaresOc:
                                    break
                                move_x_temp+=move_x
                                move_y_temp+=move_y
                                move_x_temp = move_x
                                move_y_temp = move_y
                            while BLACKPIECES[piece].x+move_x_temp < 8 and BLACKPIECES[piece].y+move_y_temp < 8:
                                if (BLACKPIECES[piece].x+move_x_temp, BLACKPIECES[piece].y+move_y_temp) in blackSquaresOc:
                                    break
                                screen.blit(DOTG, ((BLACKPIECES[piece].x+move_x_temp)*WIDTH/BOARDSIZE, (BLACKPIECES[piece].y+move_y_temp)*HEIGHT/BOARDSIZE))
                                BLACKPIECES[piece].posMoves.append((BLACKPIECES[piece].x+move_x_temp, BLACKPIECES[piece].y+move_y_temp))
                                if (BLACKPIECES[piece].x+move_x_temp, BLACKPIECES[piece].y+move_y_temp) in whiteSquaresOc:
                                    break
                                move_x_temp+=move_x
                                move_y_temp+=move_y

                        else:
                            if move_mod == 's':
                                if BLACKPIECES[piece].start:
                                    if not ((BLACKPIECES[piece].x+move_x, BLACKPIECES[piece].y+move_y) in blackSquaresOc or BLACKPIECES[piece].x+move_x > 8 or BLACKPIECES[piece].y+move_y > 8):
                                        screen.blit(DOTG, ((BLACKPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (BLACKPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))
                                        BLACKPIECES[piece].posMoves.append((BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y-move_y))
                                    if not ((BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y+move_y) in blackSquaresOc or BLACKPIECES[piece].x-move_x <= 0 or BLACKPIECES[piece].y+move_y > 8):
                                        screen.blit(DOTG, ((BLACKPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (BLACKPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))
                                        BLACKPIECES[piece].posMoves.append((BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y-move_y))
                                    if not ((BLACKPIECES[piece].x+move_x, BLACKPIECES[piece].y-move_y) in blackSquaresOc or BLACKPIECES[piece].x+move_x > 8 or BLACKPIECES[piece].y-move_y <= 0):
                                        screen.blit(DOTG, ((BLACKPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (BLACKPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))
                                        BLACKPIECES[piece].posMoves.append((BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y-move_y))
                                    if not ((BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y-move_y) in blackSquaresOc or BLACKPIECES[piece].x-move_x <= 0 or BLACKPIECES[piece].y-move_y <= 0):
                                        screen.blit(DOTG, ((BLACKPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (BLACKPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))
                                        BLACKPIECES[piece].posMoves.append((BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y-move_y))
                            elif move_mod == 'n':
                                if not ((BLACKPIECES[piece].x+move_x, BLACKPIECES[piece].y+move_y) in blackSquaresOc or BLACKPIECES[piece].x+move_x >= 8 or BLACKPIECES[piece].y+move_y >= 8):
                                    screen.blit(DOTG, ((BLACKPIECES[piece].x+move_x)*WIDTH/BOARDSIZE, (BLACKPIECES[piece].y+move_y)*HEIGHT/BOARDSIZE))
                                    BLACKPIECES[piece].posMoves.append((BLACKPIECES[piece].x+move_x, BLACKPIECES[piece].y+move_y))
                                if not ((BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y+move_y) in blackSquaresOc or BLACKPIECES[piece].x-move_x < 0 or BLACKPIECES[piece].y+move_y >= 8):
                                    screen.blit(DOTG, ((BLACKPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (BLACKPIECES[piece].y+move_y)*HEIGHT/BOARDSIZE))
                                    BLACKPIECES[piece].posMoves.append((BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y+move_y))
                                if not ((BLACKPIECES[piece].x+move_x, BLACKPIECES[piece].y-move_y) in blackSquaresOc or BLACKPIECES[piece].x+move_x >= 8 or BLACKPIECES[piece].y-move_y < 0):
                                    screen.blit(DOTG, ((BLACKPIECES[piece].x+move_x)*WIDTH/BOARDSIZE, (BLACKPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))
                                    BLACKPIECES[piece].posMoves.append((BLACKPIECES[piece].x+move_x, BLACKPIECES[piece].y-move_y))
                                if not ((BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y-move_y) in blackSquaresOc or BLACKPIECES[piece].x-move_x < 0 or BLACKPIECES[piece].y-move_y < 0):
                                    screen.blit(DOTG, ((BLACKPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (BLACKPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))
                                    BLACKPIECES[piece].posMoves.append((BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y-move_y))

                    else:
                        if move_mod == 's':
                            if BLACKPIECES[piece].start:
                                if (BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y+move_y) not in whiteSquaresOc and (BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y+move_y-1) not in whiteSquaresOc and (BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y+move_y) not in blackSquaresOc and BLACKPIECES[piece].y+move_y < 8:
                                    screen.blit(DOTG, ((BLACKPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (BLACKPIECES[piece].y+move_y)*HEIGHT/BOARDSIZE))
                        elif move_mod == 'c':
                            if (BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y+move_y) in whiteSquaresOc and BLACKPIECES[piece].y+move_y < 8 and BLACKPIECES[piece].x-move_x >= 0:
                                screen.blit(DOTG, ((BLACKPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, 
                                                    (BLACKPIECES[piece].y+move_y)*HEIGHT/BOARDSIZE))
                            if (BLACKPIECES[piece].x+move_x, BLACKPIECES[piece].y+move_y) in whiteSquaresOc and BLACKPIECES[piece].y+move_y < 8 and BLACKPIECES[piece].x+move_x < 8:
                                screen.blit(DOTG, ((BLACKPIECES[piece].x+move_x)*WIDTH/BOARDSIZE, 
                                                    (BLACKPIECES[piece].y+move_y)*HEIGHT/BOARDSIZE))
                        else:
                            if (BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y+move_y) not in whiteSquaresOc and (BLACKPIECES[piece].x-move_x, BLACKPIECES[piece].y+move_y) not in blackSquaresOc:
                                screen.blit(DOTG, ((BLACKPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, 
                                                    (BLACKPIECES[piece].y+move_y)*HEIGHT/BOARDSIZE))
        ################# White #####################
        else:
            if WHITEPIECES[piece].enabled:
                for move in WHITEPIECES[piece].moves:
                    move_x = int(move[0])
                    move_y = int(move[1])
                    move_mod = move[2]
                    move_x_temp = move_x
                    move_y_temp = move_y
                    if WHITEPIECES[piece].isPawn == False:
                        if WHITEPIECES[piece].fullBoard:
                            while WHITEPIECES[piece].x-move_x_temp >= 0 and WHITEPIECES[piece].y-move_y_temp >= 0:
                                if (WHITEPIECES[piece].x-move_x_temp, WHITEPIECES[piece].y-move_y_temp) in whiteSquaresOc:
                                    break
                                screen.blit(DOTG, ((WHITEPIECES[piece].x-move_x_temp)*WIDTH/BOARDSIZE, (WHITEPIECES[piece].y-move_y_temp)*HEIGHT/BOARDSIZE))
                                if (WHITEPIECES[piece].x-move_x_temp, WHITEPIECES[piece].y-move_y_temp) in blackSquaresOc:
                                    break
                                move_x_temp+=move_x
                                move_y_temp+=move_y
                                move_x_temp = move_x
                                move_y_temp = move_y
                            while WHITEPIECES[piece].x-move_x_temp >= 0 and WHITEPIECES[piece].y+move_y_temp < 8:
                                if (WHITEPIECES[piece].x-move_x_temp, WHITEPIECES[piece].y+move_y_temp) in whiteSquaresOc:
                                    break
                                screen.blit(DOTG, ((WHITEPIECES[piece].x-move_x_temp)*WIDTH/BOARDSIZE, (WHITEPIECES[piece].y+move_y_temp)*HEIGHT/BOARDSIZE))
                                if (WHITEPIECES[piece].x-move_x_temp, WHITEPIECES[piece].y+move_y_temp) in blackSquaresOc:
                                    break
                                move_x_temp+=move_x
                                move_y_temp+=move_y
                                move_x_temp = move_x
                                move_y_temp = move_y
                            while WHITEPIECES[piece].x+move_x_temp < 8 and WHITEPIECES[piece].y-move_y_temp >= 0:
                                if (WHITEPIECES[piece].x+move_x_temp, WHITEPIECES[piece].y-move_y_temp) in whiteSquaresOc:
                                    break
                                screen.blit(DOTG, ((WHITEPIECES[piece].x+move_x_temp)*WIDTH/BOARDSIZE, (WHITEPIECES[piece].y-move_y_temp)*HEIGHT/BOARDSIZE))
                                if (WHITEPIECES[piece].x+move_x_temp, WHITEPIECES[piece].y-move_y_temp) in blackSquaresOc:
                                    break
                                move_x_temp+=move_x
                                move_y_temp+=move_y
                                move_x_temp = move_x
                                move_y_temp = move_y
                            while WHITEPIECES[piece].x+move_x_temp < 8 and WHITEPIECES[piece].y+move_y_temp < 8:
                                if (WHITEPIECES[piece].x+move_x_temp, WHITEPIECES[piece].y+move_y_temp) in whiteSquaresOc:
                                    break
                                screen.blit(DOTG, ((WHITEPIECES[piece].x+move_x_temp)*WIDTH/BOARDSIZE, (WHITEPIECES[piece].y+move_y_temp)*HEIGHT/BOARDSIZE))
                                if (WHITEPIECES[piece].x+move_x_temp, WHITEPIECES[piece].y+move_y_temp) in blackSquaresOc:
                                    break
                                move_x_temp+=move_x
                                move_y_temp+=move_y

                        else:
                            if move_mod == 's':
                                if WHITEPIECES[piece].start:
                                    if not ((WHITEPIECES[piece].x+move_x, WHITEPIECES[piece].y+move_y) in whiteSquaresOc or WHITEPIECES[piece].x+move_x > 8 or WHITEPIECES[piece].y+move_y > 8):
                                        screen.blit(DOTG, ((WHITEPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (WHITEPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))
                                    if not ((WHITEPIECES[piece].x-move_x, WHITEPIECES[piece].y+move_y) in whiteSquaresOc or WHITEPIECES[piece].x-move_x <= 0 or WHITEPIECES[piece].y+move_y > 8):
                                        screen.blit(DOTG, ((WHITEPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (WHITEPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))
                                    if not ((WHITEPIECES[piece].x+move_x, WHITEPIECES[piece].y-move_y) in whiteSquaresOc or WHITEPIECES[piece].x+move_x > 8 or WHITEPIECES[piece].y-move_y <= 0):
                                        screen.blit(DOTG, ((WHITEPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (WHITEPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))
                                    if not ((WHITEPIECES[piece].x-move_x, WHITEPIECES[piece].y-move_y) in whiteSquaresOc or WHITEPIECES[piece].x-move_x <= 0 or WHITEPIECES[piece].y-move_y <= 0):
                                        screen.blit(DOTG, ((WHITEPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (WHITEPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))

                            elif move_mod == 'n':
                                if not ((WHITEPIECES[piece].x+move_x, WHITEPIECES[piece].y+move_y) in whiteSquaresOc or WHITEPIECES[piece].x+move_x > 8 or WHITEPIECES[piece].y+move_y > 8):
                                    screen.blit(DOTG, ((WHITEPIECES[piece].x+move_x)*WIDTH/BOARDSIZE, (WHITEPIECES[piece].y+move_y)*HEIGHT/BOARDSIZE))
                                if not ((WHITEPIECES[piece].x-move_x, WHITEPIECES[piece].y+move_y) in whiteSquaresOc or WHITEPIECES[piece].x-move_x <= 0 or WHITEPIECES[piece].y+move_y > 8):
                                    screen.blit(DOTG, ((WHITEPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (WHITEPIECES[piece].y+move_y)*HEIGHT/BOARDSIZE))
                                if not ((WHITEPIECES[piece].x+move_x, WHITEPIECES[piece].y-move_y) in whiteSquaresOc or WHITEPIECES[piece].x+move_x > 8 or WHITEPIECES[piece].y-move_y <= 0):
                                    screen.blit(DOTG, ((WHITEPIECES[piece].x+move_x)*WIDTH/BOARDSIZE, (WHITEPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))
                                if not ((WHITEPIECES[piece].x-move_x, WHITEPIECES[piece].y-move_y) in whiteSquaresOc or WHITEPIECES[piece].x-move_x <= 0 or WHITEPIECES[piece].y-move_y <= 0):
                                    screen.blit(DOTG, ((WHITEPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (WHITEPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))

                    else:
                        if move_mod == 's':
                            if WHITEPIECES[piece].start:
                                if (WHITEPIECES[piece].x-move_x, WHITEPIECES[piece].y-move_y) not in blackSquaresOc and (WHITEPIECES[piece].x-move_x, WHITEPIECES[piece].y-move_y+1) not in blackSquaresOc and (WHITEPIECES[piece].x-move_x, WHITEPIECES[piece].y-move_y) not in whiteSquaresOc and WHITEPIECES[piece].y-move_y >= 0:
                                    screen.blit(DOTG, ((WHITEPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, (WHITEPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))
                        elif move_mod == 'c':
                            if (WHITEPIECES[piece].x-move_x, WHITEPIECES[piece].y-move_y) in blackSquaresOc and WHITEPIECES[piece].y-move_y >= 0 and WHITEPIECES[piece].x-move_x >= 0:
                                screen.blit(DOTG, ((WHITEPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, 
                                                   (WHITEPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))
                            if (WHITEPIECES[piece].x+move_x, WHITEPIECES[piece].y-move_y) in blackSquaresOc and WHITEPIECES[piece].y-move_y >= 0 and WHITEPIECES[piece].x+move_x < 8:
                                screen.blit(DOTG, ((WHITEPIECES[piece].x+move_x)*WIDTH/BOARDSIZE, 
                                                   (WHITEPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))
                        else:
                            if (WHITEPIECES[piece].x-move_x, WHITEPIECES[piece].y-move_y) not in blackSquaresOc and (WHITEPIECES[piece].x-move_x, WHITEPIECES[piece].y-move_y) not in whiteSquaresOc:
                                screen.blit(DOTG, ((WHITEPIECES[piece].x-move_x)*WIDTH/BOARDSIZE, 
                                                   (WHITEPIECES[piece].y-move_y)*HEIGHT/BOARDSIZE))

class pawn(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["01n", "02s", "11c"], False, True)

class knight(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["12n", "21n"], False)

class bishop(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["11n"])

class rook(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["01n", "10n"])

class queen(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["01n", "10n", "11n"])

class king(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["10n", "01n", "11n"], False)

def setup():
    global BKG, BQG, BRG, BBG, BNG, BPG, WKG, WQG, WRG, WBG, WNG, WPG, DOTG
    #Black pieces
    BKG = pygame.image.load("./BK.png")
    # BKrect = BK.get_rect()
    BQG = pygame.image.load("./BQ.png")
    # BQrect = BQ.get_rect()
    BRG = pygame.image.load("./BR.png")
    # BRrect = BR.get_rect()
    BBG = pygame.image.load("./BB.png")
    # BBrect = BB.get_rect()
    BNG = pygame.image.load("./BN.png")
    # BNrect = BN.get_rect()
    BPG = pygame.image.load("./BP.png")
    # BPrect = BP.get_rect()

    #White pieces
    WKG = pygame.image.load("./WK.png")
    # WKrect = BK.get_rect()
    WQG = pygame.image.load("./WQ.png")
    # WQrect = WQ.get_rect()
    WRG = pygame.image.load("./WR.png")
    # WRrect = WR.get_rect()
    WBG = pygame.image.load("./WB.png")
    # WBrect = WB.get_rect()
    WNG = pygame.image.load("./WN.png")
    # WNrect = WN.get_rect()
    WPG = pygame.image.load("./WP.png")
    # WPrect = WP.get_rect()

    dot = pygame.image.load("./dot.png")

    BKG = pygame.transform.scale(BKG, (WIDTH/8, HEIGHT/8))
    BQG = pygame.transform.scale(BQG, (WIDTH/8, HEIGHT/8))
    BRG = pygame.transform.scale(BRG, (WIDTH/8, HEIGHT/8))
    BBG = pygame.transform.scale(BBG, (WIDTH/8, HEIGHT/8))
    BNG = pygame.transform.scale(BNG, (WIDTH/8, HEIGHT/8))
    BPG = pygame.transform.scale(BPG, (WIDTH/8, HEIGHT/8))

    WKG = pygame.transform.scale(WKG, (WIDTH/8, HEIGHT/8))
    WQG = pygame.transform.scale(WQG, (WIDTH/8, HEIGHT/8))
    WRG = pygame.transform.scale(WRG, (WIDTH/8, HEIGHT/8))
    WBG = pygame.transform.scale(WBG, (WIDTH/8, HEIGHT/8))
    WNG = pygame.transform.scale(WNG, (WIDTH/8, HEIGHT/8))
    WPG = pygame.transform.scale(WPG, (WIDTH/8, HEIGHT/8))
    DOTG = pygame.transform.scale(dot, (WIDTH/8, HEIGHT/8))

def main():
    global BLACKPIECES, WHITEPIECES
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")
    setup()

    BLACKPIECES.append(king(4, 0, BKG))
    BLACKPIECES.append(queen(3, 0, BQG))
    BLACKPIECES.append(rook(0, 0, BRG))
    BLACKPIECES.append(rook(7, 0, BRG))
    BLACKPIECES.append(bishop(2, 0, BBG))
    BLACKPIECES.append(bishop(5, 0, BBG))
    BLACKPIECES.append(knight(6, 0, BNG))
    BLACKPIECES.append(knight(1, 0, BNG))
    BLACKPIECES.append(pawn(0, 1, BPG))
    BLACKPIECES.append(pawn(1, 1, BPG))
    BLACKPIECES.append(pawn(2, 1, BPG))
    BLACKPIECES.append(pawn(3, 1, BPG))
    BLACKPIECES.append(pawn(4, 1, BPG))
    BLACKPIECES.append(pawn(5, 1, BPG))
    BLACKPIECES.append(pawn(6, 1, BPG))
    BLACKPIECES.append(pawn(7, 1, BPG))

    WHITEPIECES.append(king(4, 7, WKG))
    WHITEPIECES.append(queen(3, 7, WQG))
    WHITEPIECES.append(rook(0, 7, WRG))
    WHITEPIECES.append(rook(7, 7, WRG))
    WHITEPIECES.append(bishop(2, 7, WBG))
    WHITEPIECES.append(bishop(5, 7, WBG))
    WHITEPIECES.append(knight(6, 7, WNG))
    WHITEPIECES.append(knight(1, 7, WNG))
    WHITEPIECES.append(pawn(0, 6, WPG))
    WHITEPIECES.append(pawn(1, 6, WPG))
    WHITEPIECES.append(pawn(2, 6, WPG))
    WHITEPIECES.append(pawn(3, 6, WPG))
    WHITEPIECES.append(pawn(4, 6, WPG))
    WHITEPIECES.append(pawn(5, 6, WPG))
    WHITEPIECES.append(pawn(6, 6, WPG))
    WHITEPIECES.append(pawn(7, 6, WPG))

    mouse_x, mouse_y = -1, -1
    whiteTurn = True #White's turn first
    highlightSquare = False

    #Game Loop#
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        darkSquare = True

        #Get area of mouse click
        if pygame.mouse.get_pressed()[0]:
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]

        #Draw board
        for x in range(BOARDSIZE):
            darkSquare = not darkSquare
            for y in range(BOARDSIZE):
                if x*WIDTH/BOARDSIZE < mouse_x and (x+1)*WIDTH/BOARDSIZE > mouse_x and y*HEIGHT/BOARDSIZE < mouse_y and (y+1)*HEIGHT/BOARDSIZE > mouse_y and mouse_x != -1 and highlightSquare:
                    pygame.draw.rect(screen, (131, 151, 106), [WIDTH/BOARDSIZE*x, HEIGHT/BOARDSIZE*y, WIDTH/BOARDSIZE, HEIGHT/BOARDSIZE])
                    darkSquare = not darkSquare

                elif darkSquare:
                    pygame.draw.rect(screen, (191, 136, 99), [WIDTH/BOARDSIZE*x, HEIGHT/BOARDSIZE*y, WIDTH/BOARDSIZE, HEIGHT/BOARDSIZE])
                    darkSquare = False
                else:
                    pygame.draw.rect(screen, (240, 217, 181), [WIDTH/BOARDSIZE*x, HEIGHT/BOARDSIZE*y, WIDTH/BOARDSIZE, HEIGHT/BOARDSIZE])
                    darkSquare = True

        #Test to see if area clicked should be highlighted. Based on occupied square by player
        highlightSquare = False
        if not whiteTurn:
            for piece in range(len(BLACKPIECES)):
                if BLACKPIECES[piece].x*WIDTH/BOARDSIZE < mouse_x and (BLACKPIECES[piece].x+1)*WIDTH/BOARDSIZE > mouse_x and BLACKPIECES[piece].y*HEIGHT/BOARDSIZE < mouse_y and (BLACKPIECES[piece].y+1)*HEIGHT/BOARDSIZE > mouse_y:
                    highlightSquare = True
                    BLACKPIECES[piece].enabled = True
                else:
                    BLACKPIECES[piece].enabled = False
        else:
            for piece in range(len(WHITEPIECES)):
                if WHITEPIECES[piece].x*WIDTH/BOARDSIZE < mouse_x and (WHITEPIECES[piece].x+1)*WIDTH/BOARDSIZE > mouse_x and WHITEPIECES[piece].y*HEIGHT/BOARDSIZE < mouse_y and (WHITEPIECES[piece].y+1)*HEIGHT/BOARDSIZE > mouse_y:
                    highlightSquare = True
                    WHITEPIECES[piece].enabled = True
                else:
                    WHITEPIECES[piece].enabled = False

        blackSquaresOc, whiteSquaresOc = list(), list()
        ### Draw pieces ###
        for piece in BLACKPIECES:
            screen.blit(piece.graphic, (piece.x*WIDTH/BOARDSIZE, piece.y*HEIGHT/BOARDSIZE))
            blackSquaresOc.append((piece.x, piece.y))
        for piece in WHITEPIECES:
            screen.blit(piece.graphic, (piece.x*WIDTH/BOARDSIZE, piece.y*HEIGHT/BOARDSIZE))
            whiteSquaresOc.append((piece.x, piece.y))

        ### Move dots ###
        for piece in BLACKPIECES:
            piece.getMoves(screen, blackSquaresOc, whiteSquaresOc)
        for piece in WHITEPIECES:
            piece.getMoves(screen, blackSquaresOc, whiteSquaresOc)

        pygame.display.flip()



if __name__ == "__main__":
    # pdb.set_trace()
    main()
    # print("--- %s seconds ---" % (time.time() - start_time))
