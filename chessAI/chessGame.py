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

    blackPieces = []
    blackPieces.append(king(4,0, BKG))
    blackPieces.append(queen(3,0, BQG))
    blackPieces.append(rook(0,0, BRG))
    blackPieces.append(rook(7,0, BRG))
    blackPieces.append(bishop(2,0, BBG))
    blackPieces.append(bishop(5,0, BBG))
    blackPieces.append(knight(6,0, BNG))
    blackPieces.append(knight(1,0, BNG))
    blackPieces.append(pawn(0,1, BPG))
    blackPieces.append(pawn(1,1, BPG))
    blackPieces.append(pawn(2,1, BPG))
    blackPieces.append(pawn(3,1, BPG))
    blackPieces.append(pawn(4,1, BPG))
    blackPieces.append(pawn(5,1, BPG))
    blackPieces.append(pawn(6,1, BPG))
    blackPieces.append(pawn(7,1, BPG))

    whitePieces = []
    whitePieces.append(king(4,7, WKG))
    whitePieces.append(queen(3,7, WQG))
    whitePieces.append(rook(0,7, WRG))
    whitePieces.append(rook(7,7, WRG))
    whitePieces.append(bishop(2,7, WBG))
    whitePieces.append(bishop(5,7, WBG))
    whitePieces.append(knight(6,7, WNG))
    whitePieces.append(knight(1,7, WNG))
    whitePieces.append(pawn(0,6, WPG))
    whitePieces.append(pawn(1,6, WPG))
    whitePieces.append(pawn(2,6, WPG))
    whitePieces.append(pawn(3,6, WPG))
    whitePieces.append(pawn(4,6, WPG))
    whitePieces.append(pawn(5,6, WPG))
    whitePieces.append(pawn(6,6, WPG))
    whitePieces.append(pawn(7,6, WPG))

    # BK1 = king(4,0, BKG)
    # BQ1 = queen(3,0, BQG)
    # BR1 = rook(0,0, BRG)
    # BR2 = rook(7,0, BRG)
    # BB1 = bishop(2,0, BBG)
    # BB2 = bishop(5,0, BBG)
    # BN1 = knight(1,0, BNG)
    # BN2 = knight(6,0, BNG)
    # BP1 = pawn(0,1, BPG)
    # BP2 = pawn(1,1, BPG)
    # BP3 = pawn(2,1, BPG)
    # BP4 = pawn(3,1, BPG)
    # BP5 = pawn(4,1, BPG)
    # BP6 = pawn(5,1, BPG)
    # BP7 = pawn(6,1, BPG)
    # BP8 = pawn(7,1, BPG)
    # WK1 = king(4,7, WKG)
    # WQ1 = queen(3,7, WQG)
    # WR1 = rook(0,7, WRG)
    # WR2 = rook(7,7, WRG)
    # WB1 = bishop(2,7, WBG)
    # WB2 = bishop(5,7, WBG)
    # WN1 = knight(1,7, WNG)
    # WN2 = knight(6,7, WNG)
    # WP1 = pawn(0,6, WPG)
    # WP2 = pawn(1,6, WPG)
    # WP3 = pawn(2,6, WPG)
    # WP4 = pawn(3,6, WPG)
    # WP5 = pawn(4,6, WPG)
    # WP6 = pawn(5,6, WPG)
    # WP7 = pawn(6,6, WPG)
    # WP8 = pawn(7,6, WPG)

    mouse_x, mouse_y = -1,-1
    whiteTurn = True #White's turn first
    highlightSquare = False

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

        #Get area of mouse click
        if pygame.mouse.get_pressed()[0]:
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]

        #Test to see if area clicked should be highlighted. Based on occupied square by player
        highlightSquare = False
        if not whiteTurn:
            for piece in blackPieces:
                if piece.x*width/boardSize < mouse_x and (piece.x+1)*width/boardSize > mouse_x and piece.y*height/boardSize < mouse_y and (piece.y+1)*height/boardSize > mouse_y:
                    highlightSquare = True
                    break
        else:
            for piece in whitePieces:
                if piece.x*width/boardSize < mouse_x and (piece.x+1)*width/boardSize > mouse_x and piece.y*height/boardSize < mouse_y and (piece.y+1)*height/boardSize > mouse_y:
                    highlightSquare = True
                    break

        for x in range(boardSize):
            darkSquare = not darkSquare
            for y in range(boardSize):
                if x*width/boardSize < mouse_x and (x+1)*width/boardSize > mouse_x and y*height/boardSize < mouse_y and (y+1)*height/boardSize > mouse_y and mouse_x != -1 and highlightSquare:
                    pygame.draw.rect(screen, (131,151,106), [width/boardSize*x,height/boardSize*y,width/boardSize, height/boardSize])
                    darkSquare = not darkSquare

                elif darkSquare:
                    pygame.draw.rect(screen, (191,136,99), [width/boardSize*x,height/boardSize*y,width/boardSize, height/boardSize])
                    darkSquare = False
                else:
                    pygame.draw.rect(screen, (240,217,181), [width/boardSize*x,height/boardSize*y,width/boardSize, height/boardSize])
                    darkSquare = True

        ### Draw Pieces ###
        for piece in blackPieces:
            screen.blit(piece.graphic,(piece.x*width/boardSize,piece.y*height/boardSize))
        for piece in whitePieces:
            screen.blit(piece.graphic,(piece.x*width/boardSize,piece.y*height/boardSize))

        pygame.display.flip()

if __name__ == "__main__":
    # pdb.set_trace()
    main()
    # print("--- %s seconds ---" % (time.time() - start_time))
