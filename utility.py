import pygame
from constants import *
from log import log


class Printer:

    def __init__(self):

        self.fonts: dict[str, pygame.font.Font] = {}

    def load_font(self, font: str = None, size: int = 20):

        key = str(font) + str(size)

        log.log(f'Loading new font {key}')

        self.fonts[key] = pygame.font.Font(font, size)

    def print(self, surface: pygame.Surface, pos: tuple[int, int], text: str, size: int = 20, color: str = 'black', font: str = None):

        key = str(font) + str(size)

        if key not in self.fonts.keys():
            self.load_font(font, size)

        image = self.fonts[key].render(text, False, color)

        surface.blit(image, pos)


printer = Printer()
