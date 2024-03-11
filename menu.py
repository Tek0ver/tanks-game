import pygame
from constants import *
from utility import printer


class Button(pygame.sprite.Sprite):

    def __init__(self, pos: tuple[int, int], text: str, clickable: bool = True):
        super().__init__()

        self.text = text

        self.image = self.build()
        self.rect = self.image.get_rect(topleft=pos)

        self.selected = False

    def build(self) -> pygame.Surface:

        text_surface = printer.get_text_surface(self.text)

        margin = 5

        button = pygame.Surface((
            text_surface.get_width() + margin,
            text_surface.get_height() + margin))

        button.fill('white')

        button.blit(
            text_surface,
            (margin / 2, margin / 2))

        return button

    def update(self):

        pass
