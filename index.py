import pygame
import os
from Kujundid import *
from Tekst import *

from Data import *

#See on see formaat, mis tuleb salvestada cache'i iga kord kui programm lahti tehakse
cacheBody = """{
    "programmiInfo" : {
        "font" : "Fondid/Gogh-ExtraBold.ttf"
    },

    "sündmused" : {
    
    }
}
"""

def main():
    pygame.init()

    font = "Fondid\Gogh-ExtraBold.ttf"

    #Data update
    if os.path.isfile("./Data/data.json"):
        #Programm on varem käivitunud
        UuendaCache(cacheBody)
        peamineInfo = VõtaFailist("programmiInfo")

    else:
        #Programm käivitub esimest korda
        UuendaCache(cacheBody)

    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    pikktekst = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic"
    fontObject = pygame.font.Font("Fondid/Gogh-ExtraBold.ttf", 20)
    tekst1 = Tekst(screen, "", font, (10,10,10), (0,100), 60)
    tekst2 = Tekst(screen, "", font, (10,10,10), (0,200), 60)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SalvestaFaili()

                running = False

        screen.fill("purple")
        


        hiireAsuk = pygame.mouse.get_pos()
        pygame.draw.circle(screen, "black", hiireAsuk, 10)
        tekstid = EraldaSobivaPikkusegaTekst(pikktekst, hiireAsuk[0], fontObject)
        #print(tekstid[0])
        tekst1.tekst = tekstid[0]
        tekst2.tekst = tekstid[1]
        
        tekst1.Joonista()
        tekst2.Joonista()



        
        tekst1.Joonista()

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

def testingMain():
    pygame.init()

    font = "Fondid\Gogh-ExtraBold.ttf"

    #Data update
    if os.path.isfile("./Data/data.json"):
        #Programm on varem käivitunud
        UuendaCache(cacheBody)
        peamineInfo = VõtaFailist("programmiInfo")

    else:
        #Programm käivitub esimest korda
        UuendaCache(cacheBody)

    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    pikktekst = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic"
    fontObject = pygame.font.Font("Fondid/Gogh-ExtraBold.ttf", 20)
    tekst1 = Tekst(screen, "", font, (10,10,10), (0,100), 60)
    tekst2 = Tekst(screen, "", font, (10,10,10), (0,200), 60)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SalvestaFaili()

                running = False

        screen.fill("purple")
        


        hiireAsuk = pygame.mouse.get_pos()
        pygame.draw.circle(screen, "black", hiireAsuk, 10)
        tekstid = EraldaSobivaPikkusegaTekst(pikktekst, hiireAsuk[0], fontObject)
        #print(tekstid[0])
        tekst1.tekst = tekstid[0]
        tekst2.tekst = tekstid[1]
        
        tekst1.Joonista()
        tekst2.Joonista()



        
        tekst1.Joonista()

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


main()