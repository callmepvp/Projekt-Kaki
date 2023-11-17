import pygame
from Programmiolek import ProgrammiOlek
from PIL import Image

def KorrutaRGB(TooniKordaja, RGB):
    heledamRGB = tuple(min(int(value * TooniKordaja), 255) for value in RGB)
    return heledamRGB

def KasHiirÜmarnelinurgas(Objekt):
    kursoriPosx, kursorPosy = pygame.mouse.get_pos()
    if Objekt.asuk[0] <= kursoriPosx <= Objekt.asuk[0] + Objekt.suurus[0] and Objekt.asuk[1] <= kursorPosy <= Objekt.asuk[1] + Objekt.suurus[1]:
        return True
    else:
        return False

def GenereeriID(Olek: "ProgrammiOlek"):
    Nimekiri = Olek.sündmusteNimekiri
    #* kontrolli pikkust
    
    if len(Nimekiri) != 0:
        kasutatudID = [sündmus.id for sündmus in Nimekiri]
        sorteeritudID = sorted(kasutatudID)

        vähimPuudu = 1
        for num in sorteeritudID:
            if num == vähimPuudu:
                vähimPuudu += 1
            elif num > vähimPuudu:
                break

        return vähimPuudu
    else:
        return 1
    
# Teeb PIL image objekti pygame surface objektiks.
def PILpiltPinnaks(PILpilt):
    image_data = PILpilt.tobytes()
    image_dimensions = PILpilt.size
    pygame_surface = pygame.image.fromstring(image_data, image_dimensions, "RGBA")
    return pygame_surface