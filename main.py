# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # assign sprite groups to containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #inittialization code
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        
        
        pygame.display.flip()

        dt = clock.tick(60)/1000 #limits the framerate to 60 FPS


if __name__ == "__main__":
    main()
