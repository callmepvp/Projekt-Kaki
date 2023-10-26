import pygame
from Kujundid import *
from Tekst import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    pikktekst = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic"
    tekst1 = MitmeReaTekst(screen, pikktekst, suurus=30, reaLaius=500, asuk=(0, 600), reavahe=30, font="SVBASICMANUAL.TTF", värv=(10,10,10))

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")
        


        hiireAsuk = pygame.mouse.get_pos()
        tekst1.MuudaReaLaiust(hiireAsuk[0])


        
        tekst1.Joonista()

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


main()