import pygame.image
from pygame import Surface, Font, Rect

from Code.Const import WIN_WIDTH, MENU_OPTION, COLOR_BLACK, COLOR_RED


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.sf = pygame.image.load('./Assets/MenuArtv2.png')
        self.rect = self.sf.get_rect(left=0, top=0)

    def start(self):
        pygame.mixer.music.load('./Assets/menuSound.wav')
        pygame.mixer.music.play(-1)

        while True:
           self.screen.blit(source=self.sf, dest=self.rect)
           self.menu_text(70,"Ninja Seryu",COLOR_RED,((WIN_WIDTH/2),60))

           for i in range(len(MENU_OPTION)):
               self.menu_text(40, MENU_OPTION[i], COLOR_BLACK, ((WIN_WIDTH / 2), 250 + 40 * i))


           pygame.display.flip()

           for event in pygame.event.get():
            if event.type == pygame.QUIT:
             pygame.quit()
             quit()

    def menu_text(self,text_size: int, text: str, text_color:tuple, text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont(name="arial black", size=text_size)
        text_sf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_sf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_sf, dest=text_rect)
