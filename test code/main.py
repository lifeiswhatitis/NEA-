import pygame, sys
from settings import *
from tiles import Tile
from level import Level
from player import Player

#Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill('black')
    level.run()
    
    pygame.display.update()
    clock.tick(60)