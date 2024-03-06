import pygame
from constants import *
from log import log
from utility import printer

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True

while running:

    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    screen.fill(FILL_COLOR)
    
    # test text
    printer.print(screen, (50,50), "TEST")

    pygame.display.flip()

    clock.tick(60)
