import pygame
import painting_requests
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

draw_legend = True

while is_running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                draw_legend = not draw_legend
    
    # checking if there are new circles and drawing them
    if last_checked is None or pygame.time.get_ticks() - last_checked >= 1000:
        usuarios = painting_requests.get_users_names()
        last_checked = pygame.time.get_ticks()

    for usuario, os in usuarios:
        if usuario not in usuarios_shapes:
            usuarios_shapes[usuario] = Ball(usuario, os)
    
    window_surface.blit(background, (0, 0))

    for s in usuarios_shapes:
        usuarios_shapes[s].calculate_pos()
        usuarios_shapes[s].draw_itself(window_surface)
    
    # draw the legend
    if draw_legend:
        my_font = pygame.font.SysFont(None, 36)
        
        os_legend = {
            "Ubuntu": '#e95420',
            "Manjaro": '#34be5b',
            "Linux Mint": '#92B662',
            "Arch Linux": '#1793d1',
            "Else": '#ffffff',
        }
        
        y_offset = 200
        for os_name, color in os_legend.items():
            img = my_font.render(os_name, True, pygame.Color(color))
            window_surface.blit(img, (SCREEN_WIDTH - 175, SCREEN_HEIGHT - y_offset))
            y_offset -= 30

    pygame.display.update()
    clock.tick(144)
