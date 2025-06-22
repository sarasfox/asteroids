import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)   

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        kind = int(self.radius / ASTEROID_MIN_RADIUS)
        if kind > 1:
            angle = random.uniform(20, 50)
            speed = self.velocity.length() * 1.2
            velocity = pygame.Vector2(1, 0).rotate(angle) * speed
            velocity2 = pygame.Vector2(1, 0).rotate(-angle) * speed
            position = self.position + pygame.Vector2(1, 0).rotate(angle) * self.radius
            self.spawn(self.radius - ASTEROID_MIN_RADIUS, position, velocity)
            self.spawn(self.radius - ASTEROID_MIN_RADIUS, position, velocity2)
        super().kill()

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
        return asteroid