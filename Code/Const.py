import pygame

#C
COLOR_RED = (160,0,0)
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)

#E
EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2


ENTITY_HEALTH = {
      'stage1Bg0': 999,
      'stage1Bg1': 999,
      'stage1Bg2': 999,
      'stage1Bg3': 999,
      'stage1Bg4': 999,
      'stage1Bg5': 999,
      'stage1Bg6': 999,
      'stage2Bg0': 999,
      'stage2Bg1': 999,
      'stage2Bg2': 999,
      'stage2Bg3': 999,
      'stage2Bg4': 999,
      'stage2Bg5': 999,
      'ninjaMove1': 20,
      'Enemy1': 1,
      'Enemy2': 1,
      'Enemy3':1,
      'Enemy4':1,

}


ENTITY_SPEED = {
      'stage1Bg0': 1,
      'stage1Bg1': 2,
      'stage1Bg2': 3,
      'stage1Bg3': 4,
      'stage1Bg4': 5,
      'stage1Bg5': 6,
      'stage1Bg6': 7,
      'stage2Bg0': 0,
      'stage2Bg1': 1,
      'stage2Bg2': 2,
      'stage2Bg3': 3,
      'stage2Bg4': 4,
      'stage2Bg5': 5,
      'ninjaMove1': 5,
      'Enemy1':5,
      'Enemy2':7,
      'Enemy3':8,
      'Enemy4':10,





}

ENTITY_HIT = {
      'stage1Bg0': 0,
      'stage1Bg1': 0,
      'stage1Bg2': 0,
      'stage1Bg3': 0,
      'stage1Bg4': 0,
      'stage1Bg5': 0,
      'stage1Bg6': 0,
      'stage2Bg0': 0,
      'stage2Bg1': 0,
      'stage2Bg2': 0,
      'stage2Bg3': 0,
      'stage2Bg4': 0,
      'stage2Bg5': 0,
      'Enemy1':1,
      'Enemy2':1,
      'Enemy3':1,
      'Enemy4':1,
      'ninjaMove1':0,


}




#S

SPAWN_TIME = 2000

#T
TIMEOUT_LEVEL = 60000

TIMEOUT_STEP = 100


#M
MENU_OPTION = ('Novo Jogo',
               'Pontuação',
               'Sair')

#W
WIN_WIDTH = 800
WIN_HEIGHT = 450