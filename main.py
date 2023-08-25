import math
import random
import sys

import pygame
import time

pygame.init()
surface = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Helicopter Game")
h = surface.get_height()
w = surface.get_width()
color = (255,255,0)
clock = pygame.time.Clock()

# Create a mask from the helicopter png
gravity = 0.5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Player's upward and downward velocity
        self.vertical_velocity = 0

        original_image = pygame.image.load("helicopter.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (100, 150))
        self.rect = self.image.get_rect(center=(120, h/2))
        self.mask = pygame.mask.from_surface(pygame.transform.scale(self.image, (95, 150)))
        self.mask_image = self.mask.to_surface()

    def add_velocity(self, num):
        TERMINAL_VELOCITY = 8
        print(self.rect.y)
        if -TERMINAL_VELOCITY <= self.vertical_velocity + num <= TERMINAL_VELOCITY:
            self.vertical_velocity += num
        elif self.vertical_velocity > TERMINAL_VELOCITY:
            self.vertical_velocity = 8
        elif self.vertical_velocity < -TERMINAL_VELOCITY:
            self.vertical_velocity = -7
        self.fix_out_of_bound()

    def fix_out_of_bound(self):
        if self.rect.y < -10:
            self.vertical_velocity += 0.5
        elif self.rect.y + 150> h:
            self.vertical_velocity -= 1

    def update(self):
        self.rect.y += self.vertical_velocity


class Projectile(pygame.sprite.Sprite):
    def __init__(self, angle):
        super().__init__()
        self.x = w + 20
        self.y = h/2 + 20
        self.angle = math.radians(angle)
        self.velocity = 5
        original_image = pygame.image.load("bullet.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (20, 20))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        self.x -= self.velocity * math.cos(self.angle)
        self.rect.x = self.x
        self.y -= self.velocity * math.sin(self.angle)
        self.rect.y = self.y
        self.mask.get_rect().center = self.rect.center
        if not (-20 < self.rect.x and -20 < self.rect.y < h):
            # print(f'x: {self.x}, rect.x: {self.rect.x}')
            self.kill()

def run_game():
    running = True
    timer = 0
    increment = 2
    going_up = False
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    projectiles = pygame.sprite.Group()

    while running is True:
        clock.tick(60)
        # Remove out-of-bound projectiles
        timer += increment
        player.add_velocity(gravity)
        surface.fill('dark grey')
        all_sprites.update()
        all_sprites.draw(surface)
        if pygame.sprite.spritecollide(player, projectiles, False, pygame.sprite.collide_mask):
            break
        if timer > 5 * 60:
            projectile = Projectile(random.randrange(-25, 25))
            # projectile = Projectile(0)
            all_sprites.add(projectile)
            projectiles.add(projectile)
            increment += 0.1
            timer = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    going_up = True
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    going_up = False

        if going_up is True:
            player.add_velocity(-1)
        pygame.display.update()

    time.sleep(0.5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False

if __name__ == '__main__':
    while run_game():
        pass



