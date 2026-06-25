from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.sf = pygame.image.load('./Assets/' + name + '.png')
        self.rect = self.sf.get_rect(left=position[0], top=position[1])
        self.speed = 0


    @abstractmethod
    def move(self,):
        pass
