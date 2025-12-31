import pygame
from constants import LINE_WIDTH

class Shot:
    def __init__(self, position, velocity):
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)
        self.radius = 2

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            (255, 255, 255),
            self.position,
            self.radius,
            LINE_WIDTH
        )
