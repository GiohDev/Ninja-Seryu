import pygame

from Code.Entity import Entity
from Code.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen,name, game_level):
        self.screen = screen
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('stageBg'))


    def start(self):
          while True:
            for ent in self.entity_list:
                self.screen.blit(source=ent.sf, dest=ent.rect)
            pygame.display.flip()



