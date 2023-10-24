from Kujundid import *

def tekst(screen, tekst, font, color, x, y):
    img = font.render(tekst, True, color)
    screen.blit(img, (x, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    font = pygame.font.SysFont("C:\Windows\Fonts\ARLRDBD.TTF", 30)
    clock = pygame.time.Clock()
    running = True
    rk = Ristkülik(screen, screen)


    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")
        tekst(screen, "kms", font, (255, 0, 0), 0, 0)

        rk.Joonista()

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


main()