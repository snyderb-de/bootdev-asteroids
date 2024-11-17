import pygame
import constants
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0

    # show player as a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # rotate player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    # update player
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            # turn left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # turn right
            self.rotate(dt)



        