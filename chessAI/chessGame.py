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
dotG=None

BKrect,BQrect,BRrect,BBrect,BNrect,BPrect=None,None,None,None,None,None
WKrect,WQrect,WRrect,WBrect,WNrect,WPrect=None,None,None,None,None,None

class piece(object):
    def __init__(self, xPos, yPos, graphic, movement, fullBoard=True, pawn=False, directions="multi"):
        self.x = xPos
        self.y = yPos
        self.moves = movement
        self.fullBoard = fullBoard
        self.pawn = pawn
        self.start = True
        self.graphic = graphic
        self.enabled = False
        self.directions = directions

class pawn(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["01n","02s","11c"], False, True, "one")

class knight(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["12n","21n"], False)

class bishop(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["11n"])

class rook(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["01n","10n"])

class queen(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["01n","10n","11n"])

class king(piece):
    def __init__(self, xPos, yPos, graphic):
        piece.__init__(self, xPos, yPos, graphic, ["10n","01n","11n"], False)

def setup():
    global BKG,BQG,BRG,BBG,BNG,BPG,WKG,WQG,WRG,WBG,WNG,WPG, dotG
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

    dot = pygame.image.load("./dot.png")

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
    dotG = pygame.transform.scale(dot,(width/8,height/8))

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
    # whitePieces.append(pawn(3,6, WPG))
    # whitePieces.append(pawn(4,6, WPG))
    whitePieces.append(pawn(5,6, WPG))
    # whitePieces.append(pawn(6,6, WPG))
    # whitePieces.append(pawn(7,6, WPG))

    mouse_x, mouse_y = -1,-1
    whiteTurn = True #White's turn first
    highlightSquare = False

    #Game Loop#
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0,0,0))
        darkSquare = True

        #Get area of mouse click
        # for x in range(20):
        if pygame.mouse.get_pressed()[0]:
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]

        #Test to see if area clicked should be highlighted. Based on occupied square by player
        highlightSquare = False
        if not whiteTurn:
            for piece in range(len(blackPieces)):
                if blackPieces[piece].x*width/boardSize < mouse_x and (blackPieces[piece].x+1)*width/boardSize > mouse_x and blackPieces[piece].y*height/boardSize < mouse_y and (blackPieces[piece].y+1)*height/boardSize > mouse_y:
                    highlightSquare = True
                    blackPieces[piece].enabled = True
                else:
                    blackPieces[piece].enabled = False
        else:
            for piece in range(len(whitePieces)):
                if whitePieces[piece].x*width/boardSize < mouse_x and (whitePieces[piece].x+1)*width/boardSize > mouse_x and whitePieces[piece].y*height/boardSize < mouse_y and (whitePieces[piece].y+1)*height/boardSize > mouse_y:
                    highlightSquare = True
                    whitePieces[piece].enabled = True
                else:
                    whitePieces[piece].enabled = False

        #Draw board
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

        blackSquaresOc = []
        for piece in blackPieces:
            blackSquaresOc.append((piece.x,piece.y))

        whiteSquaresOc = []
        for piece in whitePieces:
            whiteSquaresOc.append((piece.x,piece.y))

        for piece in blackPieces:
            if piece.enabled:
                for move in piece.moves:
                    move_x = int(move[0])
                    move_y = int(move[1])
                    move_mod = move[2]
                    screen.blit(dotG,((piece.x+move_x)*width/boardSize,(piece.y+move_y)*height/boardSize))
        for piece in whitePieces:
            if piece.enabled:
                for move in piece.moves:
                    move_x = int(move[0])
                    move_y = int(move[1])
                    move_mod = move[2]
                    move_x_temp = move_x
                    move_y_temp = move_y
                    if piece.directions == "multi":
                        if piece.fullBoard:
                            while piece.x-move_x_temp >= 0 and piece.y-move_y_temp >= 0:
                                if (piece.x-move_x_temp,piece.y-move_y_temp) in whiteSquaresOc:
                                    break
                                print("here1")
                                screen.blit(dotG,((piece.x-move_x_temp)*width/boardSize,(piece.y-move_y_temp)*height/boardSize))
                                if (piece.x-move_x_temp,piece.y-move_y_temp) in blackSquaresOc:
                                    break
                                move_x_temp+=move_x
                                move_y_temp+=move_y
                            move_x_temp = move_x
                            move_y_temp = move_y
                            while piece.x-move_x_temp >= 0 and piece.y+move_y_temp < 8:
                                if (piece.x-move_x_temp,piece.y+move_y_temp) in whiteSquaresOc:
                                    break
                                print("here2")
                                screen.blit(dotG,((piece.x-move_x_temp)*width/boardSize,(piece.y+move_y)*height/boardSize))
                                if (piece.x-move_x_temp,piece.y+move_y_temp) in blackSquaresOc:
                                    break
                                move_x_temp+=move_x
                                move_y_temp+=move_y
                            move_x_temp = move_x
                            move_y_temp = move_y
                            while piece.x+move_x_temp < 8 and piece.y-move_y_temp >= 0:
                                if (piece.x+move_x_temp,piece.y-move_y_temp) in whiteSquaresOc:
                                    break
                                print("here3")
                                print(piece.x,piece.y)
                                print(move_x_temp,move_y_temp)
                                screen.blit(dotG,((piece.x+move_x_temp)*width/boardSize,(piece.y-move_y_temp)*height/boardSize))
                                if (piece.x+move_x_temp,piece.y-move_y_temp) in blackSquaresOc:
                                    break
                                move_x_temp+=move_x
                                move_y_temp+=move_y
                            move_x_temp = move_x
                            move_y_temp = move_y
                            while piece.x+move_x_temp < 8 and piece.y+move_y_temp < 8:
                                if (piece.x+move_x_temp,piece.y+move_y_temp) in whiteSquaresOc:
                                    break
                                print("here4")
                                screen.blit(dotG,((piece.x+move_x_temp)*width/boardSize,(piece.y+move_y)*height/boardSize))
                                if (piece.x+move_x_temp,piece.y+move_y_temp) in blackSquaresOc:
                                    break
                                move_x_temp+=move_x
                                move_y_temp+=move_y

                        else:
                            if move_mod == 's':
                                if piece.start:
                                    if not ((piece.x+move_x_temp,piece.y+move_y_temp) in whiteSquaresOc or piece.x+move_x_temp > 8 or piece.y+move_y_temp > 8):
                                        screen.blit(dotG,((piece.x-move_x)*width/boardSize,(piece.y-move_y)*height/boardSize))
                                    if not ((piece.x-move_x_temp,piece.y+move_y_temp) in whiteSquaresOc or piece.x-move_x_temp <= 0 or piece.y+move_y_temp > 8):
                                        screen.blit(dotG,((piece.x-move_x)*width/boardSize,(piece.y-move_y)*height/boardSize))
                                    if not ((piece.x+move_x_temp,piece.y-move_y_temp) in whiteSquaresOc or piece.x+move_x_temp > 8 or piece.y-move_y_temp <= 0):
                                        screen.blit(dotG,((piece.x-move_x)*width/boardSize,(piece.y-move_y)*height/boardSize))
                                    if not ((piece.x-move_x_temp,piece.y-move_y_temp) in whiteSquaresOc or piece.x-move_x_temp <= 0 or piece.y-move_y_temp <= 0):
                                        screen.blit(dotG,((piece.x-move_x)*width/boardSize,(piece.y-move_y)*height/boardSize))

                            elif move_mod == 'n':
                                screen.blit(dotG,((piece.x-move_x)*width/boardSize,(piece.y-move_y)*height/boardSize))

                            elif move_mod == 'c':
                                if (piece.x-move_x, piece.y-move_y) in blackSquaresOc:
                                    screen.blit(dotG,((piece.x-move_x)*width/boardSize,(piece.y-move_y)*height/boardSize))


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
