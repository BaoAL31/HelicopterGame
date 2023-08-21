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

# Create a mask from the helicopter png

running = True
gravity = 0.3

class Projectile(pygame.sprite.Sprite):
    def __init__(self, angle):
        super().__init__()
        self.angle = angle/100
        self.velocity = 5
        original_image = pygame.image.load("bullet.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (20, 20))
        self.rect = self.image.get_rect(center=(w, h/2))
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()

    def update(self):
        self.rect.x -= self.velocity * math.cos(self.angle)
        self.rect.y -= self.velocity * math.sin(self.angle)

        if not (-w/2 < self.rect.x < w and -h < self.rect.y < h):
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("helicopter.png").convert_alpha()
        self.image = pygame.transform.scale(original_image,
                                            (original_image.get_width() / 3, original_image.get_height() / 3))
        self.rect = self.image.get_rect(center=(200, h/2))
        self.mask = pygame.mask.from_surface(self.image)
        # Player's upward and downward velocity
        self.vertical_velocity = 0

    def add_velocity(self, num):
        TERMINAL_VELOCITY = 8
        if -TERMINAL_VELOCITY <= self.vertical_velocity + num <= TERMINAL_VELOCITY:
            self.vertical_velocity += num

    def update(self):
        self.rect.y += self.vertical_velocity

if __name__ == '__main__':
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
        all_sprites.draw(surface)
        all_sprites.update()
        if pygame.sprite.spritecollide(player, projectiles, False, pygame.sprite.collide_mask):
            print("Collided!")
        if timer > 5 * 60:
            projectile = Projectile(random.randrange(-45, 45))
            all_sprites.add(projectile)
            projectiles.add(projectile)
            increment += 0.2
            timer = 0

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
            player.add_velocity(-0.6)

        pygame.display.update()





