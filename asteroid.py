import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self): 
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(random_angle)
        vel2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        pos1 = self.position.copy()
        pos2 = self.position.copy()

        asteroid1 = Asteroid(pos1.x, pos1.y, new_radius)
        asteroid1.velocity = vel1 * 1.2
        asteroid2 = Asteroid(pos2.x, pos2.y, new_radius)
        asteroid2.velocity = vel2 * 1.2

        return asteroid1, asteroid2

    def draw(self, screen):
        #Draw asteroid as a circle
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        #Update position based on velocity
        self.position += self.velocity * dt
    
            

            


    