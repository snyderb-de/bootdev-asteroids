# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            

        screen.fill((0, 0, 0))
        
        player.update(dt)
        player.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()


