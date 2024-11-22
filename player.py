import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0

    # new variable for player timer
    player_timer = 0

    # show player as a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # method for player rotation
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # method for player movement
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    # update player rotation and movement
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        # check for key presses and move accordingly
        if keys[pygame.K_a]:
            # turn left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # turn right
            self.rotate(dt)
        if keys[pygame.K_w]:
            # move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # move backward
            self.move(-dt)

        #shoot if spacebar pressed
        if keys[pygame.K_SPACE] and self.player_timer <= 0:
            self.shoot()
            # reset player timer
            self.player_timer = PLAYER_SHOOT_COOLDOWN
            Shot(self.position.x, self.position.y, SHOT_RADIUS, self.rotation)

        # decrease player timer by dt every time update is called
        self.player_timer -= dt

    # shoot method
    def shoot(self):
        Shot(self.position.x, self.position.y, SHOT_RADIUS, self.rotation)
    
    
