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

BKG,BQG,BRG,BBG,BNG,BPG=None,None,None,None,None,None
WKG,WQG,WRG,WBG,WNG,WPG=None,None,None,None,None,None

BKrect,BQrect,BRrect,BBrect,BNrect,BPrect=None,None,None,None,None,None
WKrect,WQrect,WRrect,WBrect,WNrect,WPrect=None,None,None,None,None,None

class piece(object):
    def __init__(self, xPos, yPos, graphic, movement, fullBoard=True, pawn=False):
        self.x = xPos
        self.y = yPos
        self.moves = movement
        self.fullBoard = fullBoard
        self.pawn = pawn
        self.home = True
        self.graphic = graphic

class pawn(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["y1","y2","y1x1c"], False, True)

class knight(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["y1x2","y2x1"], False)

class bishop(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["y1x1"])

class rook(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["y1","x1"])

class queen(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["y1","x1","y1x1"])

class king(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["y1","x1","y1x1"], False)

def setup():
    global BKG,BQG,BRG,BBG,BNG,BPG,WKG,WQG,WRG,WBG,WNG,WPG
    #Black Pieces
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

    #White Pieces
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
    BKG = pygame.transform.scale(BKG,(width/8,height/8))
    BQG = pygame.transform.scale(BQG,(width/8,height/8))
    BRG = pygame.transform.scale(BRG,(width/8,height/8))
    BBG = pygame.transform.scale(BBG,(width/8,height/8))
    BNG = pygame.transform.scale(BNG,(width/8,height/8))
    BPG = pygame.transform.scale(BPG,(width/8,height/8))

    WKG = pygame.transform.scale(WKG,(width/8,height/8))
    WQG = pygame.transform.scale(WQG,(width/8,height/8))
    WRG = pygame.transform.scale(WRG,(width/8,height/8))
    WBG = pygame.transform.scale(WBG,(width/8,height/8))
    WNG = pygame.transform.scale(WNG,(width/8,height/8))
    WPG = pygame.transform.scale(WPG,(width/8,height/8))

def main():
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Chess")
    setup()

    BK1 = king(4,0, BKG)
    BQ1 = queen(3,0, BQG)
    BR1 = rook(0,0, BRG)
    BR2 = rook(7,0, BRG)
    BB1 = bishop(2,0, BBG)
    BB2 = bishop(5,0, BBG)
    BN1 = knight(1,0, BNG)
    BN2 = knight(6,0, BNG)
    BP1 = pawn(0,1, BPG)
    BP2 = pawn(1,1, BPG)
    BP3 = pawn(2,1, BPG)
    BP4 = pawn(3,1, BPG)
    BP5 = pawn(4,1, BPG)
    BP6 = pawn(5,1, BPG)
    BP7 = pawn(6,1, BPG)
    BP8 = pawn(7,1, BPG)

    WK1 = king(4,7, WKG)
    WQ1 = queen(3,7, WQG)
    WR1 = rook(0,7, WRG)
    WR2 = rook(7,7, WRG)
    WB1 = bishop(2,7, WBG)
    WB2 = bishop(5,7, WBG)
    WN1 = knight(1,7, WNG)
    WN2 = knight(6,7, WNG)
    WP1 = pawn(0,6, WPG)
    WP2 = pawn(1,6, WPG)
    WP3 = pawn(2,6, WPG)
    WP4 = pawn(3,6, WPG)
    WP5 = pawn(4,6, WPG)
    WP6 = pawn(5,6, WPG)
    WP7 = pawn(6,6, WPG)
    WP8 = pawn(7,6, WPG)

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

        screen.blit(BK1.graphic,(BK1.x*width/boardSize,BK1.y*height/boardSize))
        screen.blit(BQ1.graphic,(BQ1.x*width/boardSize,BQ1.y*height/boardSize))
        screen.blit(BR1.graphic,(BR1.x*width/boardSize,BR1.y*height/boardSize))
        screen.blit(BR2.graphic,(BR2.x*width/boardSize,BR2.y*height/boardSize))
        screen.blit(BB1.graphic,(BB1.x*width/boardSize,BB1.y*height/boardSize))
        screen.blit(BB2.graphic,(BB2.x*width/boardSize,BB2.y*height/boardSize))
        screen.blit(BN1.graphic,(BN1.x*width/boardSize,BN1.y*height/boardSize))
        screen.blit(BN2.graphic,(BN2.x*width/boardSize,BN2.y*height/boardSize))

        screen.blit(BP1.graphic,(BP1.x*width/boardSize,BP1.y*height/boardSize))
        screen.blit(BP2.graphic,(BP2.x*width/boardSize,BP2.y*height/boardSize))
        screen.blit(BP3.graphic,(BP3.x*width/boardSize,BP3.y*height/boardSize))
        screen.blit(BP4.graphic,(BP4.x*width/boardSize,BP4.y*height/boardSize))
        screen.blit(BP5.graphic,(BP5.x*width/boardSize,BP5.y*height/boardSize))
        screen.blit(BP6.graphic,(BP6.x*width/boardSize,BP6.y*height/boardSize))
        screen.blit(BP7.graphic,(BP7.x*width/boardSize,BP7.y*height/boardSize))
        screen.blit(BP8.graphic,(BP8.x*width/boardSize,BP8.y*height/boardSize))


        screen.blit(WK1.graphic,(WK1.x*width/boardSize,WK1.y*height/boardSize))
        screen.blit(WQ1.graphic,(WQ1.x*width/boardSize,WQ1.y*height/boardSize))
        screen.blit(WR1.graphic,(WR1.x*width/boardSize,WR1.y*height/boardSize))
        screen.blit(WR2.graphic,(WR2.x*width/boardSize,WR2.y*height/boardSize))
        screen.blit(WB1.graphic,(WB1.x*width/boardSize,WB1.y*height/boardSize))
        screen.blit(WB2.graphic,(WB2.x*width/boardSize,WB2.y*height/boardSize))
        screen.blit(WN1.graphic,(WN1.x*width/boardSize,WN1.y*height/boardSize))
        screen.blit(WN2.graphic,(WN2.x*width/boardSize,WN2.y*height/boardSize))

        screen.blit(WP1.graphic,(WP1.x*width/boardSize,WP1.y*height/boardSize))
        screen.blit(WP2.graphic,(WP2.x*width/boardSize,WP2.y*height/boardSize))
        screen.blit(WP3.graphic,(WP3.x*width/boardSize,WP3.y*height/boardSize))
        screen.blit(WP4.graphic,(WP4.x*width/boardSize,WP4.y*height/boardSize))
        screen.blit(WP5.graphic,(WP5.x*width/boardSize,WP5.y*height/boardSize))
        screen.blit(WP6.graphic,(WP6.x*width/boardSize,WP6.y*height/boardSize))
        screen.blit(WP7.graphic,(WP7.x*width/boardSize,WP7.y*height/boardSize))
        screen.blit(WP8.graphic,(WP8.x*width/boardSize,WP8.y*height/boardSize))

        pygame.display.flip()

if __name__ == "__main__":
    # pdb.set_trace()
    main()
    # print("--- %s seconds ---" % (time.time() - start_time))
