import pygame
from constants import *


class Printer:

    def __init__(self):

        self.fonts: dict[str, pygame.font.Font] = {}

    def load_font(self, font: str = None, size: int = 20):

        key = str(font) + str(size)

        self.fonts[key] = pygame.font.Font(font, size)

    def print(self, surface: pygame.Surface, pos: tuple[int, int], text: str, size: int = 20, color: str = 'black', font: str = None):

        image = self.get_text_surface(text, size, color, font)

        surface.blit(image, pos)

    def get_text_surface(self, text: str, size: int = 20, color: str = 'black', font: str = None):

        key = str(font) + str(size)

        if key not in self.fonts.keys():
            self.load_font(font, size)

        text_surface = self.fonts[key].render(text, True, color)

        return text_surface


printer = Printer()
