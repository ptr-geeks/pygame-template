from constants import CUSTOM_EVENT, CUSTOM_EVENT2
from game_manager import GameManager
import pygame

class EventHandler():
    def __init__(self, game_manager: GameManager):
        self.game_manager = game_manager

    def handle_event(self, event: pygame.event.Event):
        if event.type == CUSTOM_EVENT:
            # do stuff
            print('hello')
        elif event.type == CUSTOM_EVENT2:
            print('hello2')
            # do some other stuff
