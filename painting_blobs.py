import pygame
import painting_requests
import random
from ball import Ball
from painting_constants import *
import time

pygame.init()

pygame.display.set_caption('Linux UPC : Install Party 2024')
window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.fill(pygame.Color('#000000'))

is_running = True

usuarios_shapes = {}

clock = pygame.time.Clock()

pygame.font.init()

last_checked = None

while is_running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    # checking if there are new circles and drawing them

    if (last_checked == None or pygame.time.get_ticks() - last_checked >= 1000):
        usuarios = painting_requests.get_users_names()
        last_checked = pygame.time.get_ticks()

    for (usuario, os) in usuarios:
        if usuario in usuarios_shapes:
            pass
        else:
            usuarios_shapes[usuario] = Ball(usuario, os)
    
    window_surface.blit(background, (0, 0))

    # pygame.draw.circle(window_surface, pygame.Color('#ffffff'), (random.randint(0, 800), random.randint(0, 800)), random.randint(50, 100))
    for s in usuarios_shapes:
        usuarios_shapes[s].calculate_pos()

        usuarios_shapes[s].draw_itself(window_surface)


    pygame.display.update()

    clock.tick(144)