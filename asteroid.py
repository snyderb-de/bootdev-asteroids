import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius,)
        self.velocity = velocity if velocity else pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # create two new asteroids based on ASTEROID_MIN_RADIUS  
        if self.radius <= ASTEROID_MIN_RADIUS:
            # remove the current asteroid
            self.kill()
        else:
            angle = random.uniform(20, 50)
            # use rotate method on asteroid's velocity to create 2 new vectors, rotated by angle and -angle.
            velocity1 = self.velocity.rotate(angle) * 1.5
            velocity2 = self.velocity.rotate(-angle) * 1.5
            # compute the new radius for the 2 new asteroids
            new_radius = self.radius / 2
            # create the 2 new asteroids at the same position as the current asteroid, the first asteroid's velocity is multiplyed by 1.5
            Asteroid(self.position.x, self.position.y, new_radius, velocity1)
            Asteroid(self.position.x, self.position.y, new_radius, velocity2)
        
            # remove the current asteroid
            self.kill()

