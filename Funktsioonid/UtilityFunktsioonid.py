import pygame
from Programmiolek import ProgrammiOlek
from PIL import Image

def KasAsukRingiSees(asukoht, ringiAsukoht, ringiRaadius):
    vahex = asukoht[0] - ringiAsukoht[0]
    vahey = asukoht[1] - ringiAsukoht[1]
    kaugus = (vahex**2 + vahey**2)**0.5
    if kaugus <= ringiRaadius:
        return True
    return False

def KorrutaRGB(TooniKordaja, RGB):
    
    heledamRGB = tuple(min(int(value * TooniKordaja), 255) for value in RGB)
    return heledamRGB


# Veidi huvitavam variant
def MuudaHeledust(liidetav, värv):
    # Kui palju on Ruumi täisminekuni
    rR = 255-värv[0]
    gR = 255-värv[1]
    bR = 255-värv[2]
    
    tegur = liidetav/(rR+gR+bR)
    
    # Uued värvid
    rU = min(255, värv[0]+rR*tegur)
    gU = min(255, värv[1]+gR*tegur)
    bU = min(255, värv[2]+bR*tegur)
    
    if len(värv) == 4:
        return (rU,gU,bU, värv[3])
    return (rU, gU, bU)

    


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


def võrdleObjektiParameetreid(obj1, obj2):
    if set(dir(obj1)) != set(dir(obj2)):
        return False

    for attribute_name in dir(obj1):
        if not attribute_name.startswith("__") and not callable(getattr(obj1, attribute_name)):
            if getattr(obj1, attribute_name) != getattr(obj2, attribute_name):
                return False
    return True
