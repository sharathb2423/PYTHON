import pygame
import os

b_bishop = pygame.image.load(os.path.join("img", "black_bishop.png"))
b_king = pygame.image.load(os.path.join("img", "black_king.png"))
b_knight = pygame.image.load(os.path.join("img", "black_knight.png"))
b_pawn = pygame.image.load(os.path.join("img", "black_pawn.png"))
b_queen = pygame.image.load(os.path.join("img", "black_queen.png"))
b_rook = pygame.image.load(os.path.join("img", "black_rook.png"))

w_bishop = pygame.image.load(os.path.join("img", "white_bishop.png"))
w_king = pygame.image.load(os.path.join("img", "white_king.png"))
w_knight = pygame.image.load(os.path.join("img", "white_knight.png"))
w_pawn = pygame.image.load(os.path.join("img", "white_pawn.png"))
w_queen = pygame.image.load(os.path.join("img", "white_queen.png"))
w_rook = pygame.image.load(os.path.join("img", "white_rook.png"))

b = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
w = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]
B, W = [], []
for img in b:
    B.append(pygame.transform.scale(img, (65, 65)))
for img in w:
    W.append(pygame.transform.scale(img, (65, 65)))
    
class Piece:
    img = -1
    rect = (113, 113, 525, 525)
    startx = rect[0]
    starty = rect[1]

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False

    def move(self):
        pass

    def isSelected(self):
        return self.selected

    def draw(self, win):
        if self.color == "w":
            draw_This = W[self.img]
        else:
            draw_This = B[self.img]

        x = round(self.startx + (self.col * self.rect[2] / 8))
        y = round(self.starty + (self.row * self.rect[2] / 8))

        win.blit(draw_This, (x, y))


class Bishop(Piece):
    img = 0

class King(Piece):
    img = 1

class Knight(Piece):
    img = 2

class Pawn(Piece):
    img = 3

class Queen(Piece):
    img = 4

class Rook(Piece):
    img = 5