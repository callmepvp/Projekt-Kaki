from Kujundid import *
from Tekst import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    font = pygame.font.SysFont("C:\Windows\Fonts\ARLRDBD.TTF", 30)
    clock = pygame.time.Clock()
    running = True
    rk = Ristkülik(screen, screen)
    tekst2 = Tekst(screen, "AAaa", värv=(10,10,10), asuk=(30, 50))

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")
        

        tekst2.Joonista()


        rk.Joonista()

        

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


main()