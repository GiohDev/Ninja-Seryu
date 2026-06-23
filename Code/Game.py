import pygame

from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Menu import Menu



class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def start(self):


        while True:
         menu = Menu(self.screen)
         menu.start()
         pass












