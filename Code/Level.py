import random
import sys

import pygame
from pygame import Font, Surface, Rect

from Code.Const import COLOR_RED, WIN_HEIGHT, COLOR_WHITE, EVENT_ENEMY, SPAWN_TIME
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory
from Code.EntityMediator import EntityMediator
from Code.Player import Player


class Level:
    def __init__(self, screen,name, game_level):
        self.timeout = 20000
        self.screen = screen
        self.game_level = game_level
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('stageBg'))
        self.entity_list.append(EntityFactory.get_entity('ninjaMove1'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def start(self):
        pygame.mixer.music.load('./Assets/stage0track.flac')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                  self.screen.blit(source=ent.sf , dest=ent.rect)
                  ent.move()



            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                      sys.exit()
                  if event.type == EVENT_ENEMY:
                      choice = random.choice(('Enemy1','Enemy2'))
                      self.entity_list.append(EntityFactory.get_entity(choice))

            self.stage_text(14,f'{self.name} Timeout: {self.timeout/ 1000 :.1f}s', COLOR_WHITE, (10,5))
            self.stage_text(14,f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10,WIN_HEIGHT - 35))
            self.stage_text(14,f'Entidades: {len(self.entity_list)}',COLOR_RED,(10,WIN_HEIGHT - 20))
            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            pass



    def stage_text(self,text_size:int, text:str, text_color:tuple,text_position:tuple ):
        text_font: Font = pygame.font.SysFont(name="arial black", size=text_size)
        text_sf: Surface = text_font.render(text, True,text_color).convert_alpha()
        text_rect: Rect = text_sf.get_rect(left=text_position[0], top=text_position[1])
        self.screen.blit(source=text_sf, dest=text_rect)




