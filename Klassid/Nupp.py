﻿import pygame
from PIL import Image, ImageFilter 
from Funktsioonid.UtilityFunktsioonid import PILpiltPinnaks, KasAsukRingiSees, MuudaHeledust
from Klassid.Tekst import MitmeReaTekst, Tekst
from Programmiolek import ProgrammiOlek
from Funktsioonid.UtilityFunktsioonid import võrdleObjektiParameetreid


# Iga nupp oleva objekti sees, näiteks päevaruudu sees, on nähtamatu nupualuse objekt, mis tegeleb hiireklõpsude tajumisega ja info andmisega selle kohta, kas ta on allavajutatud, hiir on selle kohal või tavaline. Selle põhjal ülemobjekt otsustab, mis värvi ta end joonistab.

# Selle klassi mõte on olla mingi teise klassi sees alamobjekt. Kui selle ülemklassi suurus v asukoht määratakse, peab sellesama funktsiooniga määratama ka selle nupuAluse objketi asukoht ja suurus ja need vastavaks määrama.
class NupuAlus:
    def __init__(self, olek:"ProgrammiOlek",prioriteet=0, funktsioon = None, args = None):
        self.programmiOlek = olek        
        self.pind = None
        
        # Funktsioonide määramine.
        def tühiFn(): pass
        
        if funktsioon != None: self.funktsioon = funktsioon
        else: self.funktsioon = tühiFn
            
        self.args = args
        self.nihe = (0,0)

        self.tavalineVärv = (100, 100, 100)
        self.vajutatudVärv = (70,70,70)
        self.hiirKohalVärv = (140,140,140)
        self.kasutatavVärv = self.tavalineVärv
        
        self.suurus = (500,200)
        self.asukoht = (100,100)
        self.nurgaRaadius = 0
        
        # 0 – tavaline, 1 – hiirKohal, 2 – allavajutatud
        self.olek = 0
        self.välineOlek = 0
        
        self.hiireVajutusKoht = None
        # 0 – üleval, 1 – allavajutatud
        self.eelmineHiireOlek = 0
        
        self.kasVäljaLülitatud = False
        self.prioriteet = prioriteet

    def MääraNihe(self, nihe):
        self.nihe = nihe

    def MääraVäljaLülitatus(self, väärtus:bool):
        self.kasVäljaLülitatud = väärtus

    def MääraHelendavVärv( self, värv):
        self.hiirKohalVärv = värv
       
    def MääraVajutatudVärv(self, värv):
        self.vajutatavVärv = värv

    def MääraTavalineVärv(self, värv):
        self.tavalineVärv = värv

    # Lihtsalt määrab nupule värvi vastavalt olekule. See ei oma mingit väärtust, sest nupualust ei joonistata kunagi. Välja arvatud juhul, kui spetsiaalselt joonistatakse just nupualus, et selle asukohta ja reageerimist kontrollida. 
    def RakendaOlek(self):
        if self.olek == 0:
            self.kasutatavVärv = self.tavalineVärv
        elif self.olek == 1:
            self.kasutatavVärv = self.hiirKohalVärv
        elif self.olek == 2:
            self.kasutatavVärv = self.vajutatudVärv

    # Otustab, kas hiir on nupu peal või mitte. Töötab ka siis, kui nupul on ümarad nurgad. Kui tajub, et hiir on nupu peal, ss lisab ennast programmiolekus olevasse aktiivsete nuppude nimekirja kõigile nägemiseks. NB. Kui nupp joonistatakse ümarate nurkadega ristkülikuna, ss tuleb hoolitseda, et nupualusel on täpselt sama raadiusega nurgaümardus. 
    def KasHiirKohal(self, asuk=None):
        asukx = self.asukoht[0]
        asuky = self.asukoht[1]
        suurx = self.suurus[0]
        suury = self.suurus[1]
        raad = self.nurgaRaadius
        hiireAsuk = pygame.mouse.get_pos()
        hiireAsuk = (hiireAsuk[0] - self.nihe[0], hiireAsuk[1] - self.nihe[1])
        if asuk == None:
            hiirx = hiireAsuk[0]
            hiiry = hiireAsuk[1]
        else:
            hiirx = asuk[0]
            hiiry = asuk[1]
        if hiirx > asukx+raad and hiirx < asukx + suurx-raad and hiiry > asuky and hiiry < asuky+suury or\
           hiiry > asuky+raad and hiiry < asuky + suury-raad and hiirx > asukx and hiirx < asukx+suurx or\
           (KasAsukRingiSees(hiireAsuk, (asukx+raad,asuky+raad), raad) or\
            KasAsukRingiSees(hiireAsuk, (asukx+suurx-raad, asuky+raad), raad) or\
            KasAsukRingiSees(hiireAsuk, (asukx+raad, asuky+suury-raad), raad) or\
            KasAsukRingiSees(hiireAsuk, (asukx+suurx-raad, asuky+suury-raad), raad)):
            return True
        return False
        

    # Valib nupule oleku ehk otsustab, kas nupp peaks olema tavaline – 0. Sellises olekus, et hiir on selle kohal – 1 või allavajutatud olekus – 2. Oleku väärtuse põhjal määrab rakendaOlek funktsioon nupule värvi. Kõik objektid, mis omavad endas nupualust, kasutavad seda funktsiooni, et teada saada, mis värvi nad peaks end joonistama.
    def TegeleNupuga(self):  
        
        if self.KasHiirKohal() == True:
            if len(self.programmiOlek.aktiivsedNupud) == 0:
                self.programmiOlek.aktiivsedNupud.add(self)
            else:
                LäbiKäidud = 0
                for i in self.programmiOlek.aktiivsedNupud:
                    if self.prioriteet != i.prioriteet and self.suurus != i.suurus and self.asukoht != i.asukoht:
                        LäbiKäidud += 1

                if len(self.programmiOlek.aktiivsedNupud) == LäbiKäidud:
                    self.programmiOlek.aktiivsedNupud.add(self)

            if self.olek == 2 and pygame.mouse.get_pressed()[0] == True:
                pass
            else:
                self.olek = 1
                for event in self.programmiOlek.pygameEvents:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.olek = 2
        else:
            for i in self.programmiOlek.aktiivsedNupud:
                if self.prioriteet == i.prioriteet and self.suurus == i.suurus and self.asukoht == i.asukoht:
                    self.programmiOlek.aktiivsedNupud.remove(i)
                    break

            self.olek = 0
                        
        self.RakendaOlek()
    

    # Nupule antud funktsiooni ei kutsuta mitte nupus endas nupu enda vajutuse tajumise peale, vaid programm.py failis, kus kõigist nuppudest mille peal hiir asub valitakse vajutuse hetkel välja suurima prioriteediga nupp ja seal kutsutakse võitjanupu funktsioon välja. Kasutades seda funktsiooni.
    def KutsuFunktsioon(self):
        if self.kasVäljaLülitatud == True:
            pass
        else:
            self.funktsioon()
    

    # Seda funktsiooni ei kasutata päris programmis kunagi. See on ainult debuggimiseks j kontrollimaks, kas nupualuse asukoht j suurus klapivad ülemobjekti omaga.
    def Joonista(self, pind):
        self.TegeleNupuga()
        
        pygame.draw.rect(pind, self.kasutatavVärv, (self.asukoht, self.suurus), border_radius=self.nurgaRaadius)
    

    # See on funktsioon, mida ülemobjekt küsib iga kaader enne joonistamist nupualuselt ja mille põhjal ülemobjekt valib oma värvi. Funktsioon tagastab üht kolmest väärtusest. 0 - tavaline, 1 - hiir on kohal, 2 - nupp on allavajutatud.
    def VõtaOlek(self):
        return self.olek
    
    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
       
    def MääraSuurus(self, suurus):
        self.suurus = suurus







class LisaSündmuseNupp:
    def __init__(self, olek:"ProgrammiOlek", pind:"pygame.Surface"):
        self.olek = olek
        self.pind = pind
        self.asukoht = (0,0)
        self.suurus = (200, 80)
        self.peamineVärv = olek.LisaSündmusNupuVärv
        self.sekundaarneVärv = olek.LisaSündmusNupuPlussiAluneVärv
        
        def f1(): 
            miksEiTöötaPõhjused = []
            if self.olek.TäpsemaVaatePäev != None:
                miksEiTöötaPõhjused.append("Detailsma vaate aken on prg lahti.")
            if self.olek.SündmuseLisamine == True:
                miksEiTöötaPõhjused.append("Sündmuse lisamine juba käib.")
            if len(miksEiTöötaPõhjused) == 0:
                if self.olek.tegevuseNäitamine == True: print("Sündmuse lisamine: False -> True.")
                self.olek.SündmuseLisamine = True
            else:
                if len(miksEiTöötaPõhjused) == 1 and self.olek.tegevuseNäitamine == True:
                    print("Aken ei avane, sest " + miksEiTöötaPõhjused[0].lower())
                else:
                    print("Sündmute lisamine ei alga järgmistel põhjustel: ")
                    for i in range(len(miksEiTöötaPõhjused)):
                        print("   " + str(i+1) + ". " + miksEiTöötaPõhjused[i])

        prio = self.olek.nuppudePrioriteedid["sündmuse lisamise nupp"]
        self.nupp = NupuAlus(olek, prio, f1)


        # Pluss
        Pp0 = Image.new(mode="RGBA", size=(64, 64), color=(0,0,0,0))
        Pp1 = Image.new(mode="RGBA", size=(64, 64), color=self.peamineVärv)
        Pmask = Image.open("Pildid/pluss2.png").convert('L')
        Pp3 = Image.composite(Pp1, Pp0, Pmask)

        # Dropshadow
        Dp0 = Image.new(mode="RGBA", size=(64, 64), color=(0,0,0,0))
        Dp1 = Image.new(mode="RGBA", size=(64, 64), color=(0,0,0,255))
        Dmask = Image.open("Pildid/pluss2.png").convert('L')
        Dmask = Dmask.filter(ImageFilter.GaussianBlur(3))
        Dp3 = Image.composite(Dp1, Dp0, Dmask)

        # Kokku
        valmis = Image.composite(Pp3, Dp3, Pp3)
        self.pildipind = PILpiltPinnaks(valmis)


    def MääraSuurus(self, suurus):
        self.suurus = suurus
        self.nupp.MääraSuurus(suurus)

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        self.nupp.MääraAsukoht(asukoht)
    
    def Joonista(self):
        self.nupp.TegeleNupuga()
        olek = self.nupp.VõtaOlek()
        
        origVärv = self.olek.LisaSündmusNupuVärv        
        värv = origVärv
        if olek == 0:
            värv = origVärv
        elif olek == 1:
            värv = MuudaHeledust(60, origVärv)
        else:
            värv = MuudaHeledust(-40, origVärv)

        vasakVärv = self.sekundaarneVärv
        paremVärv = värv

        suhe = 0.3
        
        kõrgus = self.suurus[1]
        vasakLaius = self.suurus[0]*suhe
        paremLaius = self.suurus[0] - vasakLaius
        paremAsukx = self.asukoht[0] + vasakLaius
        nurgaÜmardus = self.olek.suureNupuNurgaRaadius

        vasakRect = (self.asukoht[0], self.asukoht[1], vasakLaius*1.1, kõrgus)
        paremRect = (paremAsukx, self.asukoht[1], paremLaius, kõrgus)

        pildiAsukx = self.asukoht[0] + vasakLaius / 2 - self.pildipind.get_size()[0]/2
        pildiAsuky = self.asukoht[1] + kõrgus / 2 - self.pildipind.get_size()[1]/2

        pygame.draw.rect(self.pind, vasakVärv, vasakRect,
                         border_top_left_radius = nurgaÜmardus, 
                         border_bottom_left_radius = nurgaÜmardus)
        pygame.draw.rect(self.pind, paremVärv, paremRect,
                         border_top_right_radius = nurgaÜmardus, 
                         border_bottom_right_radius = nurgaÜmardus)
        
        
        self.pind.blit(self.pildipind, (pildiAsukx, pildiAsuky))
        
        
        nupuKiri = "Lisa sündmus"
        
        
        # Tekst nupu peale:
        nupuKirjaFont = self.olek.suureNupuTekstiPygFont
        
        kiri = MitmeReaTekst(self.olek, self.pind, nupuKiri, nupuKirjaFont)
        
        kiri.MääraRead(["Lisa", "sündmus"])
        kiri.MääraReavahe(self.olek.suureNupuTekstiSuurus * 1.1)
        ridadevahe = kiri.KuiPaljuRuumiOnVaja()
        
        asuky = self.asukoht[1] + self.suurus[1]/2 - ridadevahe/2
        asukx = paremAsukx + paremLaius/2
        kiri.MääraAsukoht((asukx, asuky))
        
        kiri.MääraKeskeleJoondus(True)
        
        kiri.Joonista()
        
        
