import pygame

from .image_path import get_image_path

class TestEntity(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load(get_image_path('jet.png'))
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(center=(100, 500))

    def update(self):
        self.rect.move_ip(0, -2)    