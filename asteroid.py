from circleshape import CircleShape
from constants import *
from logger import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius ,LINE_WIDTH )

    def update(self, dt: float) -> None:
         self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        rand = random.uniform(20,50)
        vec = pygame.math.Vector2.rotate(self.velocity , rand)
        neg_vec = pygame.math.Vector2.rotate(self.velocity , -rand)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position[0] , self.position[1] , new_radius)
        asteroid2 = Asteroid(self.position[0] , self.position[1] , new_radius)

        asteroid1.velocity = vec * 1.2
        asteroid2.velocity = neg_vec * 1.2
         


