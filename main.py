import pygame
from constants import *

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            
            running = False

    clock.tick(60)
