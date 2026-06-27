import pygame

#C
COLOR_RED = (160,0,0)
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)

#E
EVENT_ENEMY = pygame.USEREVENT + 1


ENTITY_HEALTH = {
      'stageBg0': 999,
      'stageBg1': 999,
      'stageBg2': 999,
      'stageBg3': 999,
      'stageBg4': 999,
      'stageBg5': 999,
      'stageBg6': 999,
      'ninjaMove1': 5,
      'Enemy1':4,
      'Enemy2':3,

}


ENTITY_SPEED = {
      'stageBg0': 0,
      'stageBg1': 1,
      'stageBg2': 2,
      'stageBg3': 3,
      'stageBg4': 4,
      'stageBg5': 5,
      'stageBg6': 6,
      'ninjaMove1': 4,
      'Enemy1':5,
      'Enemy2':7,




}



#S

SPAWN_TIME = 4000

#M
MENU_OPTION = ('Novo Jogo',
               'Pontuação',
               'Sair')

#W
WIN_WIDTH = 800
WIN_HEIGHT = 450