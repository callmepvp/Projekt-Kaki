import pygame
from Kujundid import Ristkülik
from Tekst import MitmeReaTekst, MituRidaOnVaja, Tekst, EraldaSobivaPikkusegaTekst
from Sündmus import Sündmus
from math import floor
from typing import List
from Programmiolek import ProgrammiOlek
from Kuupäev import Kuupäev
from Päev import Päev
from SündNimekFunktsioonid import *
from UtilityFunktsioonid import *

# SündmuseRida
# Vastutab loetelutäpi ja sündmuse nimest koosneva rea joonistamise eest päevaruudu sees. Kui päevaruudus on mitu sündmust, ss neid ridu on vastavalt nii mitu. Iga sündmuse jaoks 1.
class SündmuseRida:
    # Oke, mu jaoks on see süntaks uus, aga pmst see on ainus viis pythonis märkida, et sisestatud parameeter peab olema mingi kindla klassi esindaja ja kui pole, ss ei tohiks joosta. Süntaks järgmine: parameeter: "klassiNimi". Klassinimi justkui oleks tekst, aga tegelt pole.
    def __init__(self, olek:"ProgrammiOlek", pind, sündmus: "Sündmus"):
        self.olek = olek
        self.sündmus = sündmus
        self.pind = pind
        self.asukoht = (0,0)
        self.laius = 100

    def Joonista(self):
        värv = self.olek.ruuduTekstiVärv

        # Täpp
        täpiAsukx, asuky = self.asukoht[0], self.asukoht[1]
        raadius = self.olek.sündmuseReaTäpiRaadius
        pygame.draw.circle(self.pind, värv, (täpiAsukx, asuky), raadius)
        
        # Pealkiri
        täpivahe = self.olek.sündmuseReaTäpiVahe
        pealkAsukx = täpiAsukx + täpivahe
        pealkRuum = self.laius - täpivahe
        pealkTekst = self.sündmus.VõtaNimi()
        pealkFont = self.olek.sündmuseReaKirjaFont

        # See, kui mitu rida võib sündmuserida olla.
        ridu = self.olek.sündmuseReaRidu
        reavahe = self.olek.sündmuseReaReavahe
        
        tekst = MitmeReaTekst(self.olek, self.pind, pealkTekst, pealkFont)
        tekst.MääraLaius(pealkRuum)
        tekst.MääraAsukoht((pealkAsukx, self.asukoht[1]))
        tekst.MääraReavahe(reavahe)
        tekst.MääraRidadeArv(ridu)
        tekst.Joonista()    
 


    def MääraLaius(self, laius):
        self.laius = laius

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht

    def KuiPaljuRuumiOnVaja(self):
        
        täpivahe = self.olek.sündmuseReaTäpiVahe
        pealkRuum = self.laius - täpivahe
        pealkTekst = self.sündmus.VõtaNimi()
        pealkFont = self.olek.sündmuseReaKirjaFont

        # See, kui mitu rida võib sündmuserida olla.
        ridu = self.olek.sündmuseReaRidu
        reavahe = self.olek.sündmuseReaReavahe
        
        tekst = MitmeReaTekst(self.olek, self.pind, pealkTekst, pealkFont)
        tekst.MääraLaius(pealkRuum)
        tekst.MääraReavahe(reavahe)
        tekst.MääraRidadeArv(ridu)
        
        tulemus = tekst.KuiPaljuRuumiOnVaja()
        return tulemus
        
        


# PäevaPealkiri
class PäevaPealkiri:
    def __init__(self, olek:"ProgrammiOlek", pind, kuupäev:"Kuupäev"):
        self.kpFont = olek.päevaruuduPealkKpPygFont
        self.aFont = olek.päevaruuduPealkAastaPygFont
        self.kuupäev = kuupäev
        self.asukoht = (0,0)
        self.pind = pind
        self.värv = olek.ruuduTekstiVärv
        self.päevaAastaVahe = olek.päevaruuduPealkPäevaAastaVahe

    def MääraAsukoht(self, x, y):
        self.asukoht = (x,y)

    def Joonista(self):
        pk = self.kuupäev.VõtaPäevKuuTekstina()
        a = self.kuupäev.VõtaAastaTekstina()

        päevKuuTekst = Tekst(self.pind, pk, self.kpFont, self.värv)
        päevKuuTekst.MääraAsukoht(self.asukoht)
        päevKuuTekst.Joonista()
        
        aAsuk = (self.asukoht[0] + self.kpFont.size(pk)[0] + 10, self.asukoht[1])
        aastaTekst = Tekst(self.pind, a, self.aFont, self.värv)
        aastaTekst.MääraAsukoht(aAsuk)
        aastaTekst.Joonista()

    def VõtaLaius(self):
        pk = self.kuupäev.VõtaPäevKuuTekstina()
        a = self.kuupäev.VõtaAastaTekstina()

        laius = self.kpFont.size(pk)[0] + self.päevaAastaVahe + self.aFont.size(a)[0]
        return laius




# PäevaRuut
class PäevaRuut:
    def __init__(self, olek:"ProgrammiOlek", pind, päev:"Päev"):
        self.kuupäev = päev.kuupäev
        self.suurus = (10,10)
        self.asuk = (10,10)
        self.pealkiri = PäevaPealkiri(olek, pind, self.kuupäev)
        self.olek = olek

        self.originaalVärv = olek.päevaruuduVärv
        self.HoverTooniKordaja = olek.hoverTooniKordaja
    
        self.taust = Ristkülik(pind, self.asuk, self.suurus)
        self.pind = pind
        self.sündmused = päev.sündmusteNimekiri
        
    def MääraAsukoht(self, x, y):
        self.asuk = (x,y)

    def MääraSuurus(self, x, y):
        if x != None: self.suurus = (x, self.suurus[1])
        if y != None: self.suurus = (self.suurus[0], y)


    # Seda on vaja kutsuda peale seda, kui on määratud ruudu laius. Seda meetodit kasutab päevaruudustik, et saada teada, kui kõrgeks on mõistlik teha üks päevaruutude rida. Päevaruudustik uurib selle funktsiooni abil, mis on ruumivajaduse seis sama rea teistel ruutudel ja selle järgi valib mingi kõrguse, mis keskmiselt sobiks kõigile rea ruutudele ja mille see siis tegelikult annab igale ruudule joonistamiseks. On crazy, kui see lõpuks töötab kah.
    # Meetod uurib välja, kui kõrge oleks ruut antud laiuse korral. Kõrgus oleneb peamiselt sellest kui mitu sündmuserida on ja kui palju kordi need sündmuseread peavad enda joonistamisel uuele reale minema. Aga sellele liituvad veel kuupäeva ja teksti vahe, ruudu alumise ja ülemise osa kaugused ülemisest tekstist, alumisest tekstist, ridade vahede suurused ja mõni muu kaugus veel.
    def KuiPaljuRuumiOnVaja(self):
        ülevalt = self.olek.päevaruuduPealkKaugusÜlaservast
        ridaKuupäevast = self.olek.sündmuseReadKuupäevast
        sündmuseRidadeRead = 0
        
        täpivahe = self.olek.sündmuseReaTäpiVahe
        for i in self.sündmused:
            uusRida = SündmuseRida(self.olek, self.pind, i)
            laius = self.suurus[0] - täpivahe
            uusRida.MääraLaius(laius)
            sündmuseRidadeRead += uusRida.KuiPaljuRuumiOnVaja()
        
        ridadeVahe = (max(0, len(self.sündmused)-1)) * self.olek.sündmuseRidadeVahe
        alt = ülevalt        

        return ülevalt + ridaKuupäevast + sündmuseRidadeRead + ridadeVahe + alt


    def Joonista(self):
        #Kontrolli hiire asukohta
        if KasHiirÜmarnelinurgas(self):
            HoverVärv = KorrutaRGB(self.HoverTooniKordaja, self.originaalVärv)
            self.olek.päevaruuduVärv = HoverVärv
        else:
            self.olek.päevaruuduVärv = self.originaalVärv
            

        # Päevaruudu taust
        self.taust.MääraAsukoht(self.asuk[0], self.asuk[1])
        self.taust.MääraSuurus(self.suurus[0], self.suurus[1])
        self.taust.MääraVärv(self.olek.päevaruuduVärv)
        self.taust.Joonista()

        # Kuupäev ja aasta
        pealkAsukx = self.asuk[0] + self.olek.päevaruuduPealkKaugusVasakult
        pealkAsuky = self.asuk[1] + self.olek.päevaruuduPealkKaugusÜlaservast
        self.pealkiri.MääraAsukoht(pealkAsukx, pealkAsuky)
        self.pealkiri.Joonista()

        # Päevaruudu sündmused
        kuupäevast = self.olek.sündmuseReadKuupäevast
        asuky = pealkAsuky + kuupäevast
        täpivahe = self.olek.sündmuseReaTäpiVahe
        for i in self.sündmused:
            uusRida = SündmuseRida(self.olek, self.pind, i)
            uusRida.MääraAsukoht((self.asuk[0] + täpivahe, asuky))
            laius = self.suurus[0] - täpivahe
            uusRida.MääraLaius(laius)
            uusRida.Joonista()
            
            
            vahe = self.olek.sündmuseRidadeVahe
            asuky = asuky + uusRida.KuiPaljuRuumiOnVaja() + vahe
      




class PäevaRuudustik:
    def __init__(self, olek:ProgrammiOlek, pind):
        self.olek = olek
        self.pind = pind
        self.laius = 400
        self.asukoht = (0,0)
        self.päevaRuudud: List[PäevaRuut] = []
        päevad = VõtaKõikAlgusPäevad(olek.sündmusteNimekiri)
        for i in päevad:
            #print(olek.päevaruuduVärv)
            uusRuut = PäevaRuut(olek, pind, i)
            self.päevaRuudud.append(uusRuut)

    def MääraLaius(self, laius):
        self.laius = laius

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht

    def Joonista(self):
        # Tausta kõrgus leitakse selle põhjal mitu rida ruute tuleb ja see arvutatakse hiljem.
        taustaAsukx = self.asukoht[0]
        taustaAsuky = self.asukoht[1]
        taustaLaius = self.laius

        # Mitu ruutu mahub ühte ritta.
        äärevahe = self.olek.päevaruutudeTaustaJaRuutudeVahe
        ruuduvahe = self.olek.päevaruutudeVahe
        minLaius = self.olek.päevaruuduMinLaius
        # Leiab, mitu ruutu mahub ühte ritta. Põhineb sellel, et vaatab kui palju ruutudevahe suurusid saab vahemikku panna nii, et ülejäänud vahemikku ühe võrra suurema kogusega jagades ei annaks tulemust alla min laiuse.
        mituReas = 0
        mituVahet = 0
        ruum = taustaLaius-2*äärevahe
        while True:
            if (ruum - mituVahet * ruuduvahe) / (mituVahet+1) < minLaius:
                mituReas = mituVahet
                break
            else:
                mituVahet += 1
        
        # Võib olla olukord, kus aken läheb nii kitsaks, et isegi, kui reas on ainult 1 ruut, on sellel ikkagi nii vähe ruumi, et reas peaks olema null ruutu. See kood parandab olukorra ja lic lepib sellega, et ruudu laius on väiksem, kui minlaius.
        if mituReas == 0: mituReas = 1
        
        # Arvutab, kui palju ruumi jääb vahede kõrvalt ruutudele. Mis peab ühe reasoleva ruudu laius olema. 
        vahesidKokku = 2*äärevahe + (mituReas-1)*ruuduvahe
        ruudulaius = (taustaLaius - vahesidKokku)/mituReas

        # RUUTUDE PAIGUTAMINE ALGAB:

        ridadeArv = 0
        vasakServ = taustaAsukx
        ülemServ = taustaAsuky

        # KÕigile ruutudele määratakse ühtne laius.
        for i in self.päevaRuudud:
            i.MääraSuurus(ruudulaius, None)

        ridadeKõrgused = []
        reaKõrgus = 0
        counter = 0
        for i in self.päevaRuudud:
            
            # Kui ollakse paigutamisega rea alguses, käiakse läbi sellele reale tulevad ruudud ja küsitakse kui palju neil ruumi oleks vaja.
            antavRuum = 0
            if counter % (mituReas) == 0:
                ruumivajadused = []
                for j in self.päevaRuudud[counter:counter+mituReas]:
                    ruumivajadused.append(j.KuiPaljuRuumiOnVaja())
                    
                #Antavaks ruumiks määratakse vajaduste keskmine, aga vb tulevikus võib mingi intelligentsema otsustaja teha
                antavRuum = sum(ruumivajadused)/len(ruumivajadused)
                reaKõrgus = antavRuum
                ridadeKõrgused.append(reaKõrgus)
            
            
                
            mitmesTulp = counter % mituReas
            mitmesRida = floor(counter/mituReas)
            # Kui kõik ruudud on läbi käidud, ss on ridadeArv võrdne sellega, kui palju ridasid on ruudustikus. Seda väärtust kasutab taust, et oma kõrgus leida.
            ridadeArv = mitmesRida


            asukx = vasakServ + äärevahe + mitmesTulp*(ruudulaius + ruuduvahe)
            asuky = ülemServ + äärevahe + sum(ridadeKõrgused[:-1]) + max(len(ridadeKõrgused)-1, 0) * ruuduvahe

            i.MääraAsukoht(asukx, asuky)
            i.MääraSuurus(ruudulaius, reaKõrgus)
            counter += 1
        
        taustaKõrgus = 2*äärevahe + sum(ridadeKõrgused)+ (ridadeArv)*ruuduvahe

        # PAIGUTAMINE LÕPPES

        # ALGAB JOONISTAMINE

        # Taust
        taustaVärv = self.olek.päevaruutudeTaustaVärv
        nurgaRaadius = self.olek.päevaruutudeTaustaNurgaÜmardus
        pygame.draw.rect(self.pind, taustaVärv, (taustaAsukx, taustaAsuky, taustaLaius, taustaKõrgus), border_radius=nurgaRaadius)

        # Ruudud
        for i in self.päevaRuudud:
            i.Joonista()
            


  