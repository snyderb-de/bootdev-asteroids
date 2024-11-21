import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    # Method for drawing the object
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def update(self, dt):
        # sub-classes must override
        pass

    # Method for collision detection, treats the object as a circle, returns True if the object collides with another circle and False otherwise
    def check_collision(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)