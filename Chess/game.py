import pygame, os
from board import Board

board = pygame.image.load(os.path.join("img", "board_alt.png"))
board = pygame.transform.scale(board, (750, 750))


def redraw_window():
    win.blit(board, (0, 0))
    bo = Board(8, 8)
    bo.draw(win)
    pygame.display.update()

def main_menu():
    running = True

    while running is True:
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

WIDTH, HEIGHT = 750, 750
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")
main_menu()