from Kujundid import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    running = True
    rk = Ristkülik(screen, screen)


    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

  
        screen.fill("purple")

        rk.Joonista()

    
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


main()