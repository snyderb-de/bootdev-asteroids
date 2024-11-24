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
        # Determine new radius based on current size
        if self.radius == ASTEROID_MAX_RADIUS:
            # Large asteroid splits into two medium asteroids
            new_radius = ASTEROID_MAX_RADIUS - ASTEROID_MIN_RADIUS
        elif self.radius == ASTEROID_MAX_RADIUS - ASTEROID_MIN_RADIUS:
            # Medium asteroid splits into two small asteroids
            new_radius = ASTEROID_MIN_RADIUS
        else:
            # Small asteroids disappear
            print(f"Destroying small asteroid at ({self.position.x}, {self.position.y})")
            self.kill()
            return

        # Generate two new velocities rotated by random angles
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Scale up by 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2  # Scale up by 1.2

        # Debugging: Print splitting details
        print(f"Splitting asteroid at ({self.position.x}, {self.position.y}) with radius {self.radius}")
        print(f"New asteroids: radius={new_radius}, velocities={velocity1}, {velocity2}")

        # Create two new asteroids
        Asteroid(self.position.x, self.position.y, new_radius, velocity1)
        Asteroid(self.position.x, self.position.y, new_radius, velocity2)

        # Remove the current asteroid
        self.kill()
        print(f"Asteroid killed at ({self.position.x}, {self.position.y})")
