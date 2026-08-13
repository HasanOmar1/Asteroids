import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    # Player groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable , drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    # Asteroids groups
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    # AsteroidField groups
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()




    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        
        pygame.Surface.fill(screen,"black")
        updatable.update(dt)

        for c in asteroids:
            if c.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
