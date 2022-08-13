import pygame

from entities.test_entity import TestEntity

class GameManager:
    all_sprites = pygame.sprite.Group()
    example_group = pygame.sprite.Group()

    def __init__(self):
        new_entity = TestEntity()
        self.all_sprites.add(new_entity)
        self.example_group.add(new_entity)

    def update(self):
        self.example_group.update()