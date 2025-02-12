from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

import pygame

def main():
    num_pass, num_fail = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0 # seconds
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)
    asteroids_group = pygame.sprite.Group()
    Asteroid.containers = (asteroids_group, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color("black"))
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(GAME_FPS) / 1000

if __name__ == "__main__":
    main()