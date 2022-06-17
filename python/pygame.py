import pygame
import sys

pygame.init()
pygame.display.set_caption("pygame")
screen_size = width, height = 1200, 700
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

class Entity():
    
    def __init__(self, rect, color):
        self.rect = rect
        self.color = color
        self.delta = 1

    def update(self):
        if self.color[0] == 255:
            self.delta = -1
        elif self.color[0] == 0:
            self.delta = 1
        self.color = (self.color[0] + self.delta, 0, 0)

    def render_to(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

rect = pygame.Rect(25, 25, 100, 100)
white = (255, 255, 255)
black = (0, 0, 0)
entity = Entity(rect, white)
entities = [entity]

render = True
update = True
while True: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if update:
        for entity in entities:
            entity.update()

    if render:
        screen.fill(black)
        for entity in entities:
            entity.render_to(screen)
        pygame.display.flip()
    
    clock.tick(60)