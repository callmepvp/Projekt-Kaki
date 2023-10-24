import pygame

class Tekst:

    def __init__(self, pind, tekst, font="CORBEL.TTF", värv=(255,0,0), asuk=(0,0), suurus=60):
        pygfont = pygame.font.SysFont(font, suurus)
        self.pind = pind
        self.asuk = asuk
        self.img = pygfont.render(tekst, True, värv)
    
    
    def Joonista(self):
        self.pind.blit(self.img, self.asuk)
