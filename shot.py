import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 5)
       
    def draw(self, screen):
        pygame.draw.circle(screen, "purple", self.position, self.radius)   

    def update(self, dt):
        self.position += (self.velocity * dt)