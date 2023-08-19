import math
import random

import pygame
import time

pygame.init()
surface = pygame.display.set_mode((1000, 600))
h = surface.get_height()
w = surface.get_width()
color = (255,255,0)
clock = pygame.time.Clock()
running = True
gravity = 0.5

class Projectile():
    def __init__(self, angle):
        self.x = w
        self.y = h/2
        self.angle = angle/100
        self.velocity = 5

    def get_pos(self):
        return self.x, self.y
    def update(self):
        self.x -= self.velocity * math.cos(self.angle)
        self.y -= self.velocity * math.sin(self.angle)

class Player():
    def __init__(self):
        self.y = h/2
        # Player's upward and downward velocity
        self.vertical_velocity = 0

    def add_velocity(self, num):
        TERMINAL_VELOCITY = 10
        if -TERMINAL_VELOCITY <= self.vertical_velocity + num <= TERMINAL_VELOCITY:
            self.vertical_velocity += num
    def get_y(self):
        return self.y
    def update(self):
        self.y += self.vertical_velocity



if __name__ == '__main__':
    timer = 0
    increment = 1
    going_up = False
    player = Player()
    projectiles = []
    while running is True:
        clock.tick(60)
        timer += increment
        player.add_velocity(gravity)
        surface.fill('black')
        player.update()
        pygame.draw.rect(surface, 'green', pygame.Rect(200, player.get_y(), 30, 30))
        if timer > 5 * 60:
            projectiles.append(Projectile(random.randrange(-45, 45)))
            increment += 0.2
            timer = 0
        for projectile in projectiles:
            projectile.update()
            pygame.draw.circle(surface, 'white', projectile.get_pos(), 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    going_up = True
                elif event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    going_up = False
        if going_up is True:
            player.add_velocity(-1)
        pygame.display.update()





