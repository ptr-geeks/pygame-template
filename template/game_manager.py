import pygame

from entities.test_entity import TestEntity

class GameManager:
    all_sprites = pygame.sprite.Group()
    example_group = pygame.sprite.Group()
    new_entity = TestEntity()

    def __init__(self):
        self.all_sprites.add(self.new_entity)
        self.example_group.add(self.new_entity)

    def update(self):
        self.example_group.update()