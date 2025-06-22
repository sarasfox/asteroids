import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.kill_count = 0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
        return asteroid

    def increment_kill_count(self):
        """Increment the kill count when an asteroid is destroyed"""
        old_kinds = self.get_current_asteroid_kinds()
        self.kill_count += 1
        new_kinds = self.get_current_asteroid_kinds()

        # Print when asteroid kinds increase
        if new_kinds > old_kinds:
            print(f"Kill count reached {self.kill_count}! Asteroid kinds increased to {new_kinds}")

    def get_current_asteroid_kinds(self):
        """Calculate current asteroid kinds based on kill count doubling"""
        if self.kill_count == 0:
            return ASTEROID_KINDS

        # Find how many times the kill count has doubled
        # Start with 1 kill, then 2, 4, 8, 16, etc.
        doubles = 0
        threshold = 5
        while self.kill_count >= threshold:
            doubles += 1
            threshold *= 2

        # Add 1 kind for each doubling milestone reached
        return ASTEROID_KINDS + doubles

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))

            # Use dynamic asteroid kinds based on kill count
            current_kinds = self.get_current_asteroid_kinds()
            kind = random.randint(1, current_kinds)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)