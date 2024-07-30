from pygame import Color
import pygame
import random
from painting_constants import *

class Ball:
    def __init__(self, username):
        self.username = username
        self.color = Color('#ffffff')
        self.radius = BALL_RADIUS 
        self.pos = [random.randint(0, 800), random.randint(0, 800)]
        self.speed = [random.randint(-10, 10), random.randint(-10, 10)]
        self.last_calculated_pos = pygame.time.get_ticks()
    
    def draw_itself(self, window_surface):
        pygame.draw.circle(window_surface, self.color, self.pos, self.radius)

        my_font = pygame.font.SysFont(None, 24)
        img = my_font.render(self.username, True, Color('#ffffff'))
        window_surface.blit(img, (self.pos[0], self.pos[1] + 2*BALL_RADIUS))
    
    def calculate_pos(self):
        if (pygame.time.get_ticks() != 0 and pygame.time.get_ticks() != self.last_calculated_pos):
            self.pos[0] += self.speed[0]/(pygame.time.get_ticks() - self.last_calculated_pos)
            self.pos[1] += self.speed[1]/(pygame.time.get_ticks() - self.last_calculated_pos)

            self.last_calculated_pos = pygame.time.get_ticks()
        
        if (self.pos[0] > (SCREEN_WIDTH-self.radius) or self.pos[0] < self.radius):
            self.speed[0] = self.speed[0] * -1

        if (self.pos[1] > (SCREEN_HEIGHT-self.radius) or self.pos[1] < self.radius):
            self.speed[1] = self.speed[1] * -1