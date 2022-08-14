# Import the pygame module
import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from constants import BACKGROUND_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH
from event_handler import EventHandler
from game_manager import GameManager
from constants import FRAMERATE


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game_manager = GameManager()
event_handler = EventHandler(game_manager)

running = True

clock = pygame.time.Clock()

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        else:
            event_handler.handle_event(event)

    pressed_keys = pygame.key.get_pressed()

    screen.fill(BACKGROUND_COLOR)

    game_manager.update()

    for entity in game_manager.all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

    clock.tick(FRAMERATE)
