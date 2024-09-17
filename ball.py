from pygame import Color
import pygame
import random
from painting_constants import *


class Ball:
    def __init__(self, username, os):
        self.username = username
        self.os = os
        self.radius = BALL_RADIUS
        self.pos = [
            random.randint(BALL_RADIUS + 20, SCREEN_WIDTH - BALL_RADIUS - 20),
            random.randint(BALL_RADIUS + 20, SCREEN_HEIGHT - BALL_RADIUS - 20),
        ]
        self.speed = [random.randint(-10, 10), random.randint(-10, 10)]
        self.last_calculated_pos = pygame.time.get_ticks()

        if os == "Arch":
            self.color = Color("#1793d1")

        elif os == "Ubuntu":
            self.color = Color("#e95420")

        elif os == "Fedora":
            self.color = Color("#3c6eb4")

        elif os == "Linux Mint":
            self.color = Color("#92b662")

        elif os == "Debian":
            self.color = Color("#d70a53")

        elif os == "Manjaro":
            self.color = Color("#34be5b")

        else:
            self.color = Color("#ffffff")

    def draw_itself(self, window_surface):
        pygame.draw.circle(window_surface, self.color, self.pos, self.radius)

        my_font = pygame.font.SysFont(None, 24)
        img = my_font.render(self.username, True, Color("#ffffff"))
        window_surface.blit(img, (self.pos[0], self.pos[1] + 2 * BALL_RADIUS))

    def calculate_pos(self):
        if (
            pygame.time.get_ticks() != 0
            and pygame.time.get_ticks() != self.last_calculated_pos
        ):
            self.pos[0] += self.speed[0] / (
                pygame.time.get_ticks() - self.last_calculated_pos
            )
            self.pos[1] += self.speed[1] / (
                pygame.time.get_ticks() - self.last_calculated_pos
            )

            self.last_calculated_pos = pygame.time.get_ticks()

        if self.pos[0] > (SCREEN_WIDTH - self.radius) or self.pos[0] < self.radius:
            self.speed[0] = self.speed[0] * -1

        if self.pos[1] > (SCREEN_HEIGHT - self.radius) or self.pos[1] < self.radius:
            self.speed[1] = self.speed[1] * -1
