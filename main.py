# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    # Set containers before creating instances
    AsteroidField.containers = (updatables,)
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)

    # Create instances after setting containers
    asteroid_field = AsteroidField()
    player = Player(x, y)
    updatables.add(player)
    updatables.add(asteroid_field)
    drawables.add(player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for updatable in updatables:
            updatable.update(dt)

        for drawable in drawables:
            drawable.draw(screen)
        

        pygame.display.flip()
        dt = clock.tick(60) / 1000
 
if __name__ == "__main__":
    main()