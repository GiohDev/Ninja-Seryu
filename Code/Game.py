import pygame

from Code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from Code.Level import Level
from Code.Menu import Menu



class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def start(self):
        while True:
         menu = Menu(self.screen)
         menu_return = menu.start()

         if menu_return == MENU_OPTION[0]:
             level = Level(self.screen,'Floresta Nebulosa', menu_return)
             level_return = level.start()
             pass
         elif menu_return == MENU_OPTION[2]:
             pygame.quit()
             quit()
         else:
             pass














