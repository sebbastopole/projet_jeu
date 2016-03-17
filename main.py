import pygame
import time
from game_ui import UserInterface
from player import Player
from level import Level

def main():
    ui = UserInterface() #init interface utilisateur
    ui.setLevel(Level())
    ui.drawLevel()
    running = True
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            ui.event(event)
    
main()

