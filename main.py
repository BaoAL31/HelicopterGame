import pygame
import time

pygame.init()
surface = pygame.display.set_mode((1000, 600))
h = surface.get_height()
color = (255,255,0)
clock = pygame.time.Clock()
running = True
gravity = 0.5

class Player():
    def __init__(self):
        self.rect = pygame.draw.rect(surface, 'white', pygame.Rect(200, h/2, 30, 30))
        # Player's upward and downward velocity
        self.vertical_velocity = 0

    def add_velocity(self, num):
        TERMINAL_VELOCITY = 10
        if -TERMINAL_VELOCITY <= self.vertical_velocity + num <= TERMINAL_VELOCITY:
            self.vertical_velocity += num
    def get_y(self):
        return self.rect.y
    def update(self):
        self.rect.move_ip(0, self.vertical_velocity)
    def handle_keys(self):
        key = pygame.key.get_pressed()
        print(key)
        if key[pygame.K_UP]:
            self.rect.move(0, -1)
    def draw(self, surface):
        pygame.draw.rect(surface, 'white', self.rect)
    def get_rect(self):
        return self.rect

if __name__ == '__main__':
    going_up = False
    player = Player()
    while running is True:
        clock.tick(60)
        player.add_velocity(gravity)
        surface.fill('black')
        pygame.draw.rect(surface, 'green', player.get_rect())
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
        player.update()

        pygame.display.update()





