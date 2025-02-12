from constants import *
from player import Player

import pygame

def main():
    num_pass, num_fail = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0 # seconds
    clock = pygame.time.Clock()
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color("black"))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(GAME_FPS) / 1000

if __name__ == "__main__":
    main()