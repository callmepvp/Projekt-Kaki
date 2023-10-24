import pygame

from Tekst import *


class ArvupaarAknas:
    
    # Objekt võtab sisse akna objekti ja selle põhjal muudab iga
    # koordinaadi väärtuse võtmise hetkel väärtuse kõige värskemaks.
    # Objekti nimi on hägus ja mitte täpselt asukohtAknas vms, sest seda saab kasutada
    # ka näiteks õige suuruse hoidmiseks ja sel juhul nimi ei kajastaks seda, mis asi on.

    # Pygame libraryga saab teha kujundeid ainult määrates nurgapunktide asukohti pikslites.

    # Selleks, et näiteks punkt püsiks pidevalt akna keskel hoolimata sellest,
    # kas akna suurus muutub v mitte, on vaja pidevalt muuta pikslite arvu,
    # mis on punkti ja akna ääre vahel.
    
    
    def __init__(self, aken, suhex, suhey):
        self.aken = aken
        self.suhe = (suhex, suhey)

    def MuudaSuhet(self, x, y):
        self.suhe = (x, y)

    def VõtaVäärtus(self):
        aknaSuurus = self.aken.get_size()
        väärtus = (aknaSuurus[0] * self.suhe[0], aknaSuurus[1] * self.suhe[1])
        return väärtus



class Ristkülik:
    # Akent on vaja selleks, et ristkülik teaks, mis suurusega olla, pinda on
    # vaja selleks, et minna pygame süsteemis sellele pinnale ennast joonistama.
    # Pind võib olla ka aken, aga aknale joonistamisel ei võeta arvesse läbipaistvust.

    def __init__(self, aken, pind):
        self.pind = pind
        self.aken = aken
        self.asukoht = ArvupaarAknas(aken, 1/3, 1/3)
        self.suurus = ArvupaarAknas(aken, 1/3, 1/3)
        self.värv = (255, 0, 0, 255)

    def MuudaVärvi(self, r, g, b, a=255):
        self.värv = (r,g,b,a)

    def Joonista(self):
        ax = self.asukoht.VõtaVäärtus()[0]
        ay = self.asukoht.VõtaVäärtus()[1]
        sx = self.suurus.VõtaVäärtus()[0]
        sy = self.suurus.VõtaVäärtus()[1]

        pygame.draw.rect(self.pind, self.värv, pygame.Rect(ax, ay, sx, sy))





class SündmuseRida:
    def __init__(self, pind, sündmus):
        self.sündmus = sündmus
        self.pind = pind

    def Joonista():
        #võtab info:
        pealkiri = Tekst(self.pind, "ÜritusePealkiri.")
        self.sündmus.VõtaNimi()
        self.sündmus.VõtaAlgusKell()
        self.sündmus.VõtaLõppkell()

        





        
"""
class Päevaruut:
    def __init__(self, päev):
        self.sündmsued = päev.võtaSündmsed()

    def Joonista():
        for i in sündmsued:
            pass
        """