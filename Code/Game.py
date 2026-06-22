import pygame

from Code.Menu import Menu



class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(800, 600))

    def start(self):
          while True:
                menu = Menu(self.screen)
                menu.start()
                pass


           # for event in pygame.event.get():
           #     if event.type == pygame.QUIT:
           #         pygame.quit()
           #         quit()









