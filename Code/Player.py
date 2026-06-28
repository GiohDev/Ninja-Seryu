import pygame

from Code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from Code.Entity import Entity



class Player(Entity):
    def __init__(self,name  , position  ):
        super().__init__(name,position)
        self.vy = 0
        self.gravity = 0.6
        self.jump_power = -10
        self.is_jumping = False
        self.ground_y = WIN_HEIGHT - 50

    def move(self):
        pressed_key = pygame.key.get_pressed()

        # Esquerda e Direita
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        elif pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        # Pulo
        if pressed_key[pygame.K_SPACE] and not self.is_jumping:
            self.vy = self.jump_power
            self.is_jumping = True

        # Gravidade
        self.vy += self.gravity
        self.rect.centery += self.vy

        # Chão
        if self.rect.bottom >= WIN_HEIGHT - 20:
            self.rect.bottom = WIN_HEIGHT - 20
            self.vy = 0
            self.is_jumping = False















