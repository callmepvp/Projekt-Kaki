import pygame
import os

from Programmiolek import ProgrammiOlek


# Funktsioon võtab sisse teksti, pikkuse pikslites ja pygame fonti objekti.
# Funktsioon tagastab esialgse teksti kahe tekstilise tuplena, millest esimene osa on nii pikk, et mahuks täpselt antud pikkusesse ja teine osa on kõik ülejäänud tekst.
def EraldaSobivaPikkusegaTekst(algtekst, sobivPikkus, fontObject:pygame.font.Font):
    kasvatatav = ""
    for i in algtekst:
        kasvatatav += i
        laius = fontObject.size(kasvatatav)[0]
        if laius > sobivPikkus:
            return (kasvatatav[:-1], algtekst[len(kasvatatav)-1:])
    return (kasvatatav,"")



class Tekst:

    def __init__(self, pind, tekst, pygFont, värv=(255,0,0), asuk=(0,0)):
        self.pygFont = pygFont
        self.pind = pind
        self.asuk = asuk
        self.tekst = tekst
        self.värv = värv
    
    
    def Joonista(self):
        suurtäheKõrgus = self.pygFont.get_ascent()
        
        # Oke, see on scuffed ja töötab kindlalt ainult selle fondiga. 0.22 on silma järgi valitud, aga see arv aitab teha nii, et tekst joonistuks valitud kohta täpselt nii, et väiketähe kõrguse keskkoht oleks soovitud kõrgusel. Keskkoht selle pärast, et ss on bullet pointe lihtsam joondada. Seda peaks vist täiendama, kui on vaja kirjutada mitmerealine tekst. Scuffed on veel see, et height on fontide terminoloogias väiketähe kõrgus, aga siin imo on vahemik nt j tähe langusest l tähe tõusuni, seega u 2x väiketähe kõrgus.
        poolVäiketäheKõrgus = self.pygFont.get_height()*0.22
        
        tekstiAsuk = (self.asuk[0], self.asuk[1]-suurtäheKõrgus + poolVäiketäheKõrgus)

        img = self.pygFont.render(self.tekst, True, self.värv)
        self.pind.blit(img, tekstiAsuk)


    def MääraAsukoht(self, asuk):
        self.asuk = asuk

    def MääraTekst(self, tekst):
        self.tekst = tekst



class MitmeReaTekst:
    def __init__(self, olek:ProgrammiOlek, pind, tekst, pygfont):
        self.olek = olek
        self.pind = pind
        self.tekst = tekst
        self.laius = 100
        self.asukoht = (0,0)
        self.font = pygfont
        self.värv = (10,10,10,255)
        self.reavahe = 30
        # Ridade arv vastab sellele, kui mitu rida joonistatakse. Väärtus 0 tähendab, et joonistatakse nii palju ridu kui kulub kogu teksti joonistamiseks.
        self.ridadeArv = 3

    def MääraRidadeArv(self, ridu):
        self.ridadeArv = ridu

    def MääraLaius(self, laius):
        self.laius = laius
    
    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht

    def MääraVärv(self, värv):
        self.värv = värv

    def MääraReavahe(self, reavahe):
        self.reavahe = reavahe

    # Erinevalt peaaegu kõigi teiste objektide Joonista funktsioonidest see siin returnib midagi. See returnib viimase rekstirea asukoha. Kasutades seda infot saavad muud asjad väljaspool objekti end paigutada.
    def Joonista(self):

        reavahe = self.reavahe
        reafont = self.font
        värv = self.värv
        joonistadaJäänud = self.tekst

        if self.ridadeArv != 0:
            for i in range(self.ridadeArv):
                tekstid = EraldaSobivaPikkusegaTekst(joonistadaJäänud, self.laius, reafont)
                joonistatav = tekstid[0]
                joonistadaJäänud = tekstid[1]
                
                asukx = self.asukoht[0]
                asuky = self.asukoht[1] + i * reavahe
                rida = Tekst(self.pind, joonistatav, reafont, värv, (asukx, asuky))
                rida.Joonista()

                if joonistadaJäänud == "":
                    break
        else:
            while joonistadaJäänud != "":
                tekstid = EraldaSobivaPikkusegaTekst(joonistadaJäänud, self.laius, reafont)
                joonistatav = tekstid[0]
                joonistadaJäänud = tekstid[1]
                
                asukx = self.asuk[0]
                asuky = self.asuk[1] + i * reavahe
                rida = Tekst(self.pind, joonistatav, reafont, värv, (asukx, asuky))
                rida.Joonista()

        return asuky


def TekstRidadeks(tekst, pygFont, laius):
    read = []
    paar = EraldaSobivaPikkusegaTekst(tekst, laius, pygFont)
    read.append[paar]
    while paar[1] != "":
        paar = EraldaSobivaPikkusegaTekst(paar[1], laius, pygFont)
        read.append(paar)
    return read
        
        

def MituRidaOnVaja(tekst, font, laius):
    