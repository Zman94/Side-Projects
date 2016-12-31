from __future__ import print_function
import pygame, sys, time, os
import pdb
import random
import math

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sounds disabled')

width = 600
height = 600
boardSize = 8

BK,BQ,BR,BB,BN,BP=None,None,None,None,None,None
WK,WQ,WR,WB,WN,WP=None,None,None,None,None,None

BKrect,BQrect,BRrect,BBrect,BNrect,BPrect=None,None,None,None,None,None
WKrect,WQrect,WRrect,WBrect,WNrect,WPrect=None,None,None,None,None,None

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

def setup():
    global BK,BQ,BR,BB,BN,BP,WK,WQ,WR,WB,WN,WP
    #Black Pieces
    BK = pygame.image.load("./BK.png")
    BKrect = BK.get_rect()
    BQ = pygame.image.load("./BQ.png")
    BQrect = BQ.get_rect()
    BR = pygame.image.load("./BR.png")
    BRrect = BR.get_rect()
    BB = pygame.image.load("./BB.png")
    BBrect = BB.get_rect()
    BN = pygame.image.load("./BN.png")
    BNrect = BN.get_rect()
    BP = pygame.image.load("./BP.png")
    BPrect = BP.get_rect()

    #White Pieces
    WK = pygame.image.load("./WK.png")
    WKrect = BK.get_rect()
    WQ = pygame.image.load("./WQ.png")
    WQrect = WQ.get_rect()
    WR = pygame.image.load("./WR.png")
    WRrect = WR.get_rect()
    WB = pygame.image.load("./WB.png")
    WBrect = WB.get_rect()
    WN = pygame.image.load("./WN.png")
    WNrect = WN.get_rect()
    WP = pygame.image.load("./WP.png")
    WPrect = WP.get_rect()

def main():
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Chess")
    setup()

    #Game Loop#
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # elif event.type == MOUSEBUTTONUP:
            #     if event.pos == #pos
            #     #click code
        screen.fill((0,0,0))
        darkSquare = True
        for x in range(boardSize):
            darkSquare = not darkSquare
            for y in range(boardSize):
                if darkSquare:
                    pygame.draw.rect(screen, (191,136,99), [width/boardSize*x,height/boardSize*y,width/boardSize, height/boardSize])
                    darkSquare = False
                else:
                    pygame.draw.rect(screen, (240,217,181), [width/boardSize*x,height/boardSize*y,width/boardSize, height/boardSize])
                    darkSquare = True

        screen.blit(BK,(0,0))

        pygame.display.flip()

if __name__ == "__main__":
    # pdb.set_trace()
    main()
    # print("--- %s seconds ---" % (time.time() - start_time))
