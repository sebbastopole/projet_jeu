import pygame
import time
from game_ui import UserInterface
from player import Player
from level import Level

def main():
    ui = UserInterface() #init interface utilisateur
    while ui.running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            ui.running = False
        elif event.type == pygame.KEYDOWN:
            ui.keyEvent(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ui.mouseEvent(event)
main()

