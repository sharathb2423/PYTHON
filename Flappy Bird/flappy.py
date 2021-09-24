import pygame
import random

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 576, 1024
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird Game')
clock = pygame.time.Clock()


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos - 950))
    return bottom_pipe, top_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def display_score():
    score_surface = game_font.render(f'{str(score)}', 1, (255, 255, 255))
    screen.blit(score_surface, (WIDTH / 2 - score_surface.get_width() / 2, 100))


bg_surface = pygame.image.load('background-night.png')
bg_surface = pygame.transform.scale(bg_surface, (WIDTH, HEIGHT))

floor_surface = pygame.image.load('base.png')
floor_surface = pygame.transform.scale2x(floor_surface)

bird_surface = pygame.image.load('bluebird.png')
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=(100, 512))

pipe_surface = pygame.image.load('pipe.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [400, 600, 800]


running = True
floor_pos = 0
gravity = 0.25
bird_movement = 0
game_active = True
game_font = pygame.font.SysFont('consolas', 40)
score = 0
lost = False

while running is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 8

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            score += 1

    screen.blit(bg_surface, (0, 0))
    floor_pos -= 1

    for pipe in pipe_list:
        if bird_rect.colliderect(pipe):
            game_active = False
            lost = True
        if bird_rect.top <= -100 or bird_rect.bottom >= 900:
            game_active = False
            lost = True

    if lost is True:
        end_surface = pygame.image.load('gameover.png').convert_alpha()
        end_surface = pygame.transform.scale(end_surface, (300, 100))
        screen.blit(end_surface, (WIDTH / 2 - end_surface.get_width() / 2, HEIGHT / 2 - 50))

    if game_active:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)

        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        display_score()


    def draw_floor():
        screen.blit(floor_surface, (floor_pos, 900))
        screen.blit(floor_surface, (floor_pos + 576, 900))
    if floor_pos < -576: floor_pos = 0
    draw_floor()

    pygame.display.update()
    clock.tick(120)