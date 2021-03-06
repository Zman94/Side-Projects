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

BKRECT, BQRECT, BRRECT, BBRECT, BNRECT, BPRECT = None, None, None, None, None, None
WKRECT, WQRECT, WRRECT, WBRECT, WNRECT, WPRECT = None, None, None, None, None, None

class Piece(object):
    def __init__(self, xPos, yPos, graphic, movement, fullBoard=True, pawn=False):
        self.x = xPos
        self.y = yPos
        self.moves = movement
        self.fullBoard = fullBoard
        self.pawn = pawn
        self.start = True
        self.graphic = graphic
        self.enabled = False

class pawn(Piece):
    def __init__(self, xPos, yPos, graphic):
        Piece.__init__(self, xPos, yPos, graphic, ["01n", "02s", "11c"], False, True)

class knight(Piece):
    def __init__(self, xPos, yPos, graphic):
        Piece.__init__(self, xPos, yPos, graphic, ["12n", "21n"], False)

class bishop(Piece):
    def __init__(self, xPos, yPos, graphic):
        Piece.__init__(self, xPos, yPos, graphic, ["11n"])

class rook(Piece):
    def __init__(self, xPos, yPos, graphic):
        Piece.__init__(self, xPos, yPos, graphic, ["01n", "10n"])

class queen(Piece):
    def __init__(self, xPos, yPos, graphic):
        Piece.__init__(self, xPos, yPos, graphic, ["01n", "10n", "11n"])

class king(Piece):
    def __init__(self, xPos, yPos, graphic):
        Piece.__init__(self, xPos, yPos, graphic, ["10n", "01n", "11n"], False)

def setup():
    global BKG, BQG, BRG, BBG, BNG, BPG, WKG, WQG, WRG, WBG, WNG, WPG, DOTG
    #Black Pieces
    BKG = pygame.image.load("./BK.png")
    # BKRECT = BK.get_rect()
    BQG = pygame.image.load("./BQ.png")
    # BQRECT = BQ.get_rect()
    BRG = pygame.image.load("./BR.png")
    # BRRECT = BR.get_rect()
    BBG = pygame.image.load("./BB.png")
    # BBRECT = BB.get_rect()
    BNG = pygame.image.load("./BN.png")
    # BNRECT = BN.get_rect()
    BPG = pygame.image.load("./BP.png")
    # BPRECT = BP.get_rect()

    #White Pieces
    WKG = pygame.image.load("./WK.png")
    # WKRECT = BK.get_rect()
    WQG = pygame.image.load("./WQ.png")
    # WQRECT = WQ.get_rect()
    WRG = pygame.image.load("./WR.png")
    # WRRECT = WR.get_rect()
    WBG = pygame.image.load("./WB.png")
    # WBRECT = WB.get_rect()
    WNG = pygame.image.load("./WN.png")
    # WNRECT = WN.get_rect()
    WPG = pygame.image.load("./WP.png")
    # WPRECT = WP.get_rect()

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
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")
    setup()

    blackPieces = []
    blackPieces.append(king(4, 0, BKG))
    blackPieces.append(queen(3, 0, BQG))
    blackPieces.append(rook(0, 0, BRG))
    blackPieces.append(rook(7, 0, BRG))
    blackPieces.append(bishop(2, 0, BBG))
    blackPieces.append(bishop(5, 0, BBG))
    blackPieces.append(knight(6, 0, BNG))
    blackPieces.append(knight(1, 0, BNG))
    blackPieces.append(pawn(0, 1, BPG))
    blackPieces.append(pawn(1, 1, BPG))
    blackPieces.append(pawn(2, 5, BPG))
    blackPieces.append(pawn(3, 1, BPG))
    blackPieces.append(pawn(4, 1, BPG))
    blackPieces.append(pawn(5, 1, BPG))
    blackPieces.append(pawn(6, 1, BPG))
    blackPieces.append(pawn(7, 1, BPG))

    whitePieces = []
    whitePieces.append(king(4, 7, WKG))
    whitePieces.append(queen(3, 7, WQG))
    whitePieces.append(rook(0, 7, WRG))
    whitePieces.append(rook(7, 7, WRG))
    whitePieces.append(bishop(2, 7, WBG))
    whitePieces.append(bishop(5, 7, WBG))
    whitePieces.append(knight(6, 7, WNG))
    whitePieces.append(knight(1, 7, WNG))
    whitePieces.append(pawn(0, 6, WPG))
    whitePieces.append(pawn(1, 6, WPG))
    whitePieces.append(pawn(2, 6, WPG))
    whitePieces.append(pawn(3, 6, WPG))
    whitePieces.append(pawn(4, 6, WPG))
    whitePieces.append(pawn(5, 6, WPG))
    whitePieces.append(pawn(6, 6, WPG))
    whitePieces.append(pawn(7, 6, WPG))

    mouse_x, mouse_y = -1, -1
    whiteTurn = False #White's turn first
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
            for piece in range(len(blackPieces)):
                if blackPieces[piece].x*WIDTH/BOARDSIZE < mouse_x and (blackPieces[piece].x+1)*WIDTH/BOARDSIZE > mouse_x and blackPieces[piece].y*HEIGHT/BOARDSIZE < mouse_y and (blackPieces[piece].y+1)*HEIGHT/BOARDSIZE > mouse_y:
                    highlightSquare = True
                    blackPieces[piece].enabled = True
                else:
                    blackPieces[piece].enabled = False
        else:
            for piece in range(len(whitePieces)):
                if whitePieces[piece].x*WIDTH/BOARDSIZE < mouse_x and (whitePieces[piece].x+1)*WIDTH/BOARDSIZE > mouse_x and whitePieces[piece].y*HEIGHT/BOARDSIZE < mouse_y and (whitePieces[piece].y+1)*HEIGHT/BOARDSIZE > mouse_y:
                    highlightSquare = True
                    whitePieces[piece].enabled = True
                else:
                    whitePieces[piece].enabled = False

        blackSquaresOc, whiteSquaresOc = list(), list()
        ### Draw Pieces ###
        for piece in blackPieces:
            screen.blit(piece.graphic, (piece.x*WIDTH/BOARDSIZE, piece.y*HEIGHT/BOARDSIZE))
            blackSquaresOc.append((piece.x, piece.y))
        for piece in whitePieces:
            screen.blit(piece.graphic, (piece.x*WIDTH/BOARDSIZE, piece.y*HEIGHT/BOARDSIZE))
            whiteSquaresOc.append((piece.x, piece.y))

        ### Move dots ###
        if not whiteTurn:
            for piece in blackPieces:
                if piece.enabled:
                    for move in piece.moves:
                        move_x = int(move[0])
                        move_y = int(move[1])
                        move_mod = move[2]
                        move_x_temp = move_x
                        move_y_temp = move_y
                        if piece.pawn == False:
                            if piece.fullBoard:
                                while piece.x-move_x_temp >= 0 and piece.y-move_y_temp >= 0:
                                    if (piece.x-move_x_temp, piece.y-move_y_temp) in blackSquaresOc:
                                        break
                                    screen.blit(DOTG, ((piece.x-move_x_temp)*WIDTH/BOARDSIZE, (piece.y-move_y_temp)*HEIGHT/BOARDSIZE))
                                    if (piece.x-move_x_temp, piece.y-move_y_temp) in whiteSquaresOc:
                                        break
                                    move_x_temp += move_x
                                    move_y_temp += move_y
                                move_x_temp = move_x
                                move_y_temp = move_y
                                while piece.x-move_x_temp >= 0 and piece.y+move_y_temp < 8:
                                    if (piece.x-move_x_temp, piece.y+move_y_temp) in blackSquaresOc:
                                        break
                                    screen.blit(DOTG, ((piece.x-move_x_temp)*WIDTH/BOARDSIZE, (piece.y+move_y_temp)*HEIGHT/BOARDSIZE))
                                    if (piece.x-move_x_temp, piece.y+move_y_temp) in whiteSquaresOc:
                                        break
                                    move_x_temp += move_x
                                    move_y_temp += move_y
                                move_x_temp = move_x
                                move_y_temp = move_y
                                while piece.x+move_x_temp < 8 and piece.y-move_y_temp >= 0:
                                    if (piece.x+move_x_temp, piece.y-move_y_temp) in blackSquaresOc:
                                        break
                                    screen.blit(DOTG, ((piece.x+move_x_temp)*WIDTH/BOARDSIZE, (piece.y-move_y_temp)*HEIGHT/BOARDSIZE))
                                    if (piece.x+move_x_temp, piece.y-move_y_temp) in whiteSquaresOc:
                                        break
                                    move_x_temp += move_x
                                    move_y_temp += move_y
                                move_x_temp = move_x
                                move_y_temp = move_y
                                while piece.x+move_x_temp < 8 and piece.y+move_y_temp < 8:
                                    if (piece.x+move_x_temp, piece.y+move_y_temp) in blackSquaresOc:
                                        break
                                    screen.blit(DOTG, ((piece.x+move_x_temp)*WIDTH/BOARDSIZE, (piece.y+move_y_temp)*HEIGHT/BOARDSIZE))
                                    if (piece.x+move_x_temp, piece.y+move_y_temp) in whiteSquaresOc:
                                        break
                                    move_x_temp += move_x
                                    move_y_temp += move_y

                            else:
                                if move_mod == 's':
                                    if piece.start:
                                        if not ((piece.x+move_x, piece.y+move_y) in blackSquaresOc or piece.x+move_x > 8 or piece.y+move_y > 8):
                                            screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y-move_y)*HEIGHT/BOARDSIZE))
                                        if not ((piece.x-move_x, piece.y+move_y) in blackSquaresOc or piece.x-move_x <= 0 or piece.y+move_y > 8):
                                            screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y-move_y)*HEIGHT/BOARDSIZE))
                                        if not ((piece.x+move_x, piece.y-move_y) in blackSquaresOc or piece.x+move_x > 8 or piece.y-move_y <= 0):
                                            screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y-move_y)*HEIGHT/BOARDSIZE))
                                        if not ((piece.x-move_x, piece.y-move_y) in blackSquaresOc or piece.x-move_x <= 0 or piece.y-move_y <= 0):
                                            screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y-move_y)*HEIGHT/BOARDSIZE))

                                elif move_mod == 'n':
                                    if not ((piece.x+move_x, piece.y+move_y) in blackSquaresOc or piece.x+move_x >= 8 or piece.y+move_y >= 8):
                                        screen.blit(DOTG, ((piece.x+move_x)*WIDTH/BOARDSIZE, (piece.y+move_y)*HEIGHT/BOARDSIZE))
                                    if not ((piece.x-move_x, piece.y+move_y) in blackSquaresOc or piece.x-move_x < 0 or piece.y+move_y >= 8):
                                        screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y+move_y)*HEIGHT/BOARDSIZE))
                                    if not ((piece.x+move_x, piece.y-move_y) in blackSquaresOc or piece.x+move_x >= 8 or piece.y-move_y < 0):
                                        screen.blit(DOTG, ((piece.x+move_x)*WIDTH/BOARDSIZE, (piece.y-move_y)*HEIGHT/BOARDSIZE))
                                    if not ((piece.x-move_x, piece.y-move_y) in blackSquaresOc or piece.x-move_x < 0 or piece.y-move_y < 0):
                                        screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y-move_y)*HEIGHT/BOARDSIZE))

                        else:
                            if move_mod == 's':
                                if piece.start:
                                    if (piece.x-move_x, piece.y+move_y) not in whiteSquaresOc and (piece.x-move_x, piece.y+move_y) not in blackSquaresOc and piece.y+move_y < 8:
                                        screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y+move_y)*HEIGHT/BOARDSIZE))
                            elif move_mod == 'c':
                                if (piece.x-move_x, piece.y+move_y) in whiteSquaresOc and piece.y+move_y < 8 and piece.x-move_x >= 0:
                                    screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE,
                                                       (piece.y+move_y)*HEIGHT/BOARDSIZE))
                                if (piece.x+move_x, piece.y+move_y) in whiteSquaresOc and piece.y+move_y < 8 and piece.x+move_x < 8:
                                    screen.blit(DOTG, ((piece.x+move_x)*WIDTH/BOARDSIZE,
                                                       (piece.y+move_y)*HEIGHT/BOARDSIZE))
                            else:
                                if (piece.x-move_x, piece.y+move_y) not in whiteSquaresOc and (piece.x-move_x, piece.y+move_y) not in blackSquaresOc:
                                    screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE,
                                                       (piece.y+move_y)*HEIGHT/BOARDSIZE))
        ################# White #####################
        else:
            for piece in whitePieces:
                if piece.enabled:
                    for move in piece.moves:
                        move_x = int(move[0])
                        move_y = int(move[1])
                        move_mod = move[2]
                        move_x_temp = move_x
                        move_y_temp = move_y
                        if piece.pawn == False:
                            if piece.fullBoard:
                                while piece.x-move_x_temp >= 0 and piece.y-move_y_temp >= 0:
                                    if (piece.x-move_x_temp, piece.y-move_y_temp) in whiteSquaresOc:
                                        break
                                    screen.blit(DOTG, ((piece.x-move_x_temp)*WIDTH/BOARDSIZE, (piece.y-move_y_temp)*HEIGHT/BOARDSIZE))
                                    if (piece.x-move_x_temp, piece.y-move_y_temp) in blackSquaresOc:
                                        break
                                    move_x_temp += move_x
                                    move_y_temp += move_y
                                move_x_temp = move_x
                                move_y_temp = move_y
                                while piece.x-move_x_temp >= 0 and piece.y+move_y_temp < 8:
                                    if (piece.x-move_x_temp, piece.y+move_y_temp) in whiteSquaresOc:
                                        break
                                    screen.blit(DOTG, ((piece.x-move_x_temp)*WIDTH/BOARDSIZE, (piece.y+move_y_temp)*HEIGHT/BOARDSIZE))
                                    if (piece.x-move_x_temp, piece.y+move_y_temp) in blackSquaresOc:
                                        break
                                    move_x_temp += move_x
                                    move_y_temp += move_y
                                move_x_temp = move_x
                                move_y_temp = move_y
                                while piece.x+move_x_temp < 8 and piece.y-move_y_temp >= 0:
                                    if (piece.x+move_x_temp, piece.y-move_y_temp) in whiteSquaresOc:
                                        break
                                    screen.blit(DOTG, ((piece.x+move_x_temp)*WIDTH/BOARDSIZE, (piece.y-move_y_temp)*HEIGHT/BOARDSIZE))
                                    if (piece.x+move_x_temp, piece.y-move_y_temp) in blackSquaresOc:
                                        break
                                    move_x_temp += move_x
                                    move_y_temp += move_y
                                move_x_temp = move_x
                                move_y_temp = move_y
                                while piece.x+move_x_temp < 8 and piece.y+move_y_temp < 8:
                                    if (piece.x+move_x_temp, piece.y+move_y_temp) in whiteSquaresOc:
                                        break
                                    screen.blit(DOTG, ((piece.x+move_x_temp)*WIDTH/BOARDSIZE, (piece.y+move_y_temp)*HEIGHT/BOARDSIZE))
                                    if (piece.x+move_x_temp, piece.y+move_y_temp) in blackSquaresOc:
                                        break
                                    move_x_temp += move_x
                                    move_y_temp += move_y

                            else:
                                if move_mod == 's':
                                    if piece.start:
                                        if not ((piece.x+move_x, piece.y+move_y) in whiteSquaresOc or piece.x+move_x > 8 or piece.y+move_y > 8):
                                            screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y-move_y)*HEIGHT/BOARDSIZE))
                                        if not ((piece.x-move_x, piece.y+move_y) in whiteSquaresOc or piece.x-move_x <= 0 or piece.y+move_y > 8):
                                            screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y-move_y)*HEIGHT/BOARDSIZE))
                                        if not ((piece.x+move_x, piece.y-move_y) in whiteSquaresOc or piece.x+move_x > 8 or piece.y-move_y <= 0):
                                            screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y-move_y)*HEIGHT/BOARDSIZE))
                                        if not ((piece.x-move_x, piece.y-move_y) in whiteSquaresOc or piece.x-move_x <= 0 or piece.y-move_y <= 0):
                                            screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y-move_y)*HEIGHT/BOARDSIZE))

                                elif move_mod == 'n':
                                    if not ((piece.x+move_x, piece.y+move_y) in whiteSquaresOc or piece.x+move_x > 8 or piece.y+move_y > 8):
                                        screen.blit(DOTG, ((piece.x+move_x)*WIDTH/BOARDSIZE, (piece.y+move_y)*HEIGHT/BOARDSIZE))
                                    if not ((piece.x-move_x, piece.y+move_y) in whiteSquaresOc or piece.x-move_x <= 0 or piece.y+move_y > 8):
                                        screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y+move_y)*HEIGHT/BOARDSIZE))
                                    if not ((piece.x+move_x, piece.y-move_y) in whiteSquaresOc or piece.x+move_x > 8 or piece.y-move_y <= 0):
                                        screen.blit(DOTG, ((piece.x+move_x)*WIDTH/BOARDSIZE, (piece.y-move_y)*HEIGHT/BOARDSIZE))
                                    if not ((piece.x-move_x, piece.y-move_y) in whiteSquaresOc or piece.x-move_x <= 0 or piece.y-move_y <= 0):
                                        screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y-move_y)*HEIGHT/BOARDSIZE))

                        else:
                            if move_mod == 's':
                                if piece.start:
                                    if (piece.x-move_x, piece.y-move_y) not in blackSquaresOc and (piece.x-move_x, piece.y-move_y) not in whiteSquaresOc and piece.y-move_y >= 0:
                                        screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE, (piece.y-move_y)*HEIGHT/BOARDSIZE))
                            elif move_mod == 'c':
                                if (piece.x-move_x, piece.y-move_y) in blackSquaresOc and piece.y-move_y >= 0 and piece.x-move_x >= 0:
                                    screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE,
                                                       (piece.y-move_y)*HEIGHT/BOARDSIZE))
                                if (piece.x+move_x, piece.y-move_y) in blackSquaresOc and piece.y-move_y >= 0 and piece.x+move_x < 8:
                                    screen.blit(DOTG, ((piece.x+move_x)*WIDTH/BOARDSIZE,
                                                       (piece.y-move_y)*HEIGHT/BOARDSIZE))
                            else:
                                if (piece.x-move_x, piece.y-move_y) not in blackSquaresOc and (piece.x-move_x, piece.y-move_y) not in whiteSquaresOc:
                                    screen.blit(DOTG, ((piece.x-move_x)*WIDTH/BOARDSIZE,
                                                       (piece.y-move_y)*HEIGHT/BOARDSIZE))


        pygame.display.flip()

if __name__ == "__main__":
    # pdb.set_trace()
    main()
    # print("--- %s seconds ---" % (time.time() - start_time))
