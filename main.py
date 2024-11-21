# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    # Create updatable group
    update_group = pygame.sprite.Group()
    # Create drawable group
    draw_group = pygame.sprite.Group()
    # Create asteroids group
    asteroids_group = pygame.sprite.Group()
    # Add groups to player class
    Player.containers = (update_group, draw_group)
    Asteroid.containers = (asteroids_group, update_group, draw_group)
    AsteroidField.containers = (update_group)

    
    # create the screen    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # create the player
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    # create the asteroid field
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            

        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000        

        # Update all updatable objects
        for sprite in update_group:
            sprite.update(dt) 

        # Update all drawable objects
        for sprite in draw_group:
            sprite.draw(screen)
        
        #Check for collisions
        for asteroid in asteroids_group:
            if isinstance(asteroid, Asteroid) and player.check_collision(asteroid):
                print("Game Over!")
                pygame.quit()
                return

        pygame.display.flip()


if __name__ == "__main__":
    main()


