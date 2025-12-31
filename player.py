import pygame
from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    PLAYER_MOVE_SPEED,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOOT_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(CircleShape):
    containers = ()

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

        for group in self.containers:
            group.add(self)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # cooldown timer
        self.shoot_timer = max(0, self.shoot_timer - dt)

        # rotation
        if keys[pygame.K_a]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation -= PLAYER_TURN_SPEED * dt

        # movement
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        if keys[pygame.K_w]:
            self.position += direction * PLAYER_MOVE_SPEED * dt
        if keys[pygame.K_s]:
            self.position -= direction * PLAYER_MOVE_SPEED * dt

        # shooting
        if keys[pygame.K_SPACE]:
            self.shoot()

    def draw(self, screen):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = forward.rotate(120)
        left = forward.rotate(-120)
        points = [
            self.position + forward * self.radius,
            self.position + right * self.radius * 0.6,
            self.position + left * self.radius * 0.6,
        ]
        pygame.draw.polygon(screen, "white", points, LINE_WIDTH)

    def shoot(self):
        if self.shoot_timer > 0:
            return

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED
