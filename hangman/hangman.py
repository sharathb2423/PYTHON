import pygame
import math
import random
from words import words

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman Game')
letter_font = pygame.font.SysFont('consolas', 20)
word_font = pygame.font.SysFont('consolas', 35)

images = []
for i in range(7):
    image = pygame.image.load('hangman' + str(i) + '.png')
    images.append(image)

word = random.choice(words).upper()
guessed = []

radius = 20
gap = 15
letters = []

startx = 42
starty = 400
A = 65

for i in range(26):
    x = startx + gap * 2 + ((gap + radius * 2) * (i % 13))
    y = starty + ((gap + radius * 2) * (i // 13))
    letters.append([x, y, chr(A + i), True])

def draw(screen):
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(screen, (0, 0, 0), (x, y), radius, 3)
            text = letter_font.render(ltr, 1, (0, 0, 0))
            screen.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

        display_word = ''
        for letter in word:
            if letter in guessed:
                display_word += letter + '  '
            else: display_word += '-' + '  '
        text = word_font.render(display_word, 1, (0, 0, 0))
        screen.blit(text, (400, 200))

def main_menu():
    running = True
    clock = pygame.time.Clock()
    hangman_status = 0

    def redraw_window():
        screen.fill((255, 255, 255))
        screen.blit(images[hangman_status], (150, 100))
        draw(screen)
        pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    
                    if visible:
                        dis = math.sqrt((x - mx) ** 2 + (y - my) ** 2)
                        if dis < radius:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        
        if won:
            screen.fill((255, 255, 255))
            text = word_font.render('YOU WON!', 1, (0, 0, 0))
            screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(3000)
            break

        if hangman_status == 6:
            screen.fill((255, 255, 255))
            text = word_font.render('YOU LOST!', 1, (0, 0, 0))
            screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(3000)
            print(word)
            break

        redraw_window()
        clock.tick(60)

main_menu()