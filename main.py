# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
bullets = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = updatable
Shot.containers = (bullets, shots, updatable, drawable)


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Fill the screen with black
        screen.fill("black")

        updatable.update(dt)

        #Collision detection
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.collision(asteroid):
                    bullet.kill()
                    result = asteroid.split()
                    if result is not None:
                        asteroid1, asteroid2 = result
                        asteroids.add(*result)

        #Draw player
        for entity in drawable:
            entity.draw(screen)

        #Update display
        pygame.display.flip()

        #Control frame rate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()