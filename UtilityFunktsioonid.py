import pygame
from Programmiolek import ProgrammiOlek
from PIL import Image

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