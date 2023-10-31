import pygame
from Tekst import *
from Sündmused import *

class SündmuseRida:
    # Oke, mu jaoks on see süntaks uus, aga pmst see on ainus viis pythonis märkida, et sisestatud parameeter peab olema mingi kindla klassi esindaja ja kui pole, ss ei tohiks joosta. Süntaks järgmine: parameeter: "klassiNimi". Klassinimi justkui oleks tekst, aga tegelt pole.
    def __init__(self, pind, sündmus: "Sündmus", asukoht, laius):
        self.sündmus = sündmus
        self.pind = pind
        self.asukoht = asukoht
        self.nimePygFont = pygame.font.Font("Fondid/Gogh-ExtraBold.ttf", 40)
        self.ajaPygFont = pygame.font.Font("Fondid/Gogh-ExtraBold.ttf", 25)
        self.laius = laius
        self.täpiVahe = 20

    def Joonista(self):
        
        # Täpp teksti ees.
        pygame.draw.circle(self.pind, (10, 10, 10), self.asukoht, 8)

        #Pelkirja asukoht olgu täpist täpivahe px võrra edasi.
        pealkirjaAsuk = (self.asukoht[0] + self.täpiVahe, self.asukoht[1])

        # Kui on kellaaeg, siis leiab kellaaja laiuse ja joonistab kellaaja.
        ajaLaius = 0
        ajatekst = ""
        if self.sündmus.lõppKell.KasOnKell() is True:
            ajatekst = self.sündmus.lõppKell.VõtaStringina()
            ajaLaius = self.ajaPygFont.size(ajatekst)[0]
            ajaAsuk = (self.asukoht[0] + self.laius - ajaLaius, self.asukoht[1])
            kell = Tekst(self.pind, ajatekst, self.ajaPygFont, (10,10,10), ajaAsuk)
            kell.Joonista()

        # Leitakse, kui palju ruumi jääb pealkirjale täpi ja kellaaja kõrvalt.
        ruum = self.laius - self.täpiVahe - ajaLaius - 20

        # Pealkirjast valitakse osa, mis mahub leitud laiusesse.
        pealkTekst = self.sündmus.VõtaNimi()
        mahtuvTekst = EraldaSobivaPikkusegaTekst(pealkTekst, ruum, self.nimePygFont)[0]

        # Pealkirja joonistamine
        pealkiri = Tekst(self.pind, mahtuvTekst,self.nimePygFont, (10,10,10), pealkirjaAsuk)
        pealkiri.Joonista()

    def MuudaLaiust(self, laius):
        self.laius = laius
