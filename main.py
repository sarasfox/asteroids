# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    # Set containers before creating instances
    AsteroidField.containers = (updatables,)
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Shot.containers = (shots, updatables, drawables)

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

        # Display kill count and current asteroid kinds
        kill_text = font.render(f"Kills: {asteroid_field.kill_count}", True, "green")
        kinds_text = font.render(f"Asteroid Sizes: {asteroid_field.get_current_asteroid_kinds()}", True, "red")
        screen.blit(kill_text, (10, 10))
        screen.blit(kinds_text, (10, 50))

        for asteroid in asteroids:
            for shot in shots:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()
                    # Increment kill count when asteroid is destroyed
                    asteroid_field.increment_kill_count()
            if asteroid.collide(player):
                print("Game Over!")
                pygame.quit()
                return

        pygame.display.flip()
        dt = clock.tick(60) / 1000
 
if __name__ == "__main__":
    main()