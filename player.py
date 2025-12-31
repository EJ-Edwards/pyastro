import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED
from shot import Shot


class Player(CircleShape):
    containers = ()

    def __init__(self, x, y):
        super().__init__(x, y, 20)
        self.rotation = 0

        for group in self.containers:
            group.add(self)

    def update(self, dt, keys):
        # rotation
        if keys[pygame.K_a]:
            self.rotation += 180 * dt
        if keys[pygame.K_d]:
            self.rotation -= 180 * dt

        # movement
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        if keys[pygame.K_w]:
            self.position += direction * 300 * dt
        if keys[pygame.K_s]:
            self.position -= direction * 300 * dt

        # shooting
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED
