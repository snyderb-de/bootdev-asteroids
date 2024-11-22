import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, radius)
        self.rotation = rotation

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # set shot velocity
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity = forward * PLAYER_SHOOT_SPEED
        # update shot position
        self.position += self.velocity * dt