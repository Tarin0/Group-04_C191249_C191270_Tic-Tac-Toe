import pygame
import sys
import time

import tictactoe as ttt
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (246, 239, 119)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.SysFont("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.SysFont("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.SysFont("OpenSans-Regular.ttf", 60)

user = None
board = ttt.initial_state()
ai_turn = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Let user choose a player.
    if user is None:

        # Draw title
        title = largeFont.render("Play Tic-Tac-Toe", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)