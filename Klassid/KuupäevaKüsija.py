import pygame
from Klassid.Tekstikast import SelgitavTekstikast
from Programmiolek import ProgrammiOlek
from Klassid.Kuupäev import Kuupäev

class KuupäevaKüsija:
    def __init__(self, olek:"ProgrammiOlek", pind:"pygame.Surface"):
        # Tüüpilised omadused
        self.olek = olek
        self.pind = pind
        self.suurus = (100,100)
        self.asukoht = (0,0)
        
        # Veakontrollifunktsioon
        def intKontroll(a):
            try:
                int(a)
                return True
            except:
                return False
        
        # Alamobjektid
        # Päevakast
        self.pKast = SelgitavTekstikast(olek, pind)
        def pNupuF():
            self.LõpetaKõigiKirjutamine()
            self.pKast.kast.AlustaKirjutamist()
        self.pKast.MääraNupuF(pNupuF)
        self.pKast.tekst.MääraRidadeArv(1)
        self.pKast.MääraVeaKontrolliFunktsioon(intKontroll)
        self.pKast.MääraSõnum("Päev:")
        self.pKast.MääraKeskeleJoondus(True)
        self.pKast.MääraSelgitusKastiSees(True)
        
        # Kuukast
        self.kKast = SelgitavTekstikast(olek, pind)
        def kNupuF():
            self.LõpetaKõigiKirjutamine()
            self.kKast.kast.AlustaKirjutamist()
        self.kKast.MääraNupuF(kNupuF)
        self.kKast.tekst.MääraRidadeArv(1)
        self.kKast.MääraVeaKontrolliFunktsioon(intKontroll)
        self.kKast.MääraSõnum("Kuu:")
        self.kKast.MääraKeskeleJoondus(True)
        self.kKast.MääraSelgitusKastiSees(True)
        
        # Aastakast
        self.aKast = SelgitavTekstikast(olek, pind)
        def aNupuF():
            self.LõpetaKõigiKirjutamine()
            self.aKast.kast.AlustaKirjutamist()
        self.aKast.MääraNupuF(aNupuF)
        self.aKast.tekst.MääraRidadeArv(1)
        self.aKast.MääraVeaKontrolliFunktsioon(intKontroll)
        self.aKast.MääraSõnum("Aasta:")
        self.aKast.MääraKeskeleJoondus(True)
        self.aKast.MääraSelgitusKastiSees(True)
        
    # Kirjutamise lõpetamise funktsioon. See funktsioon lõpetab selle objekti asjade kirjutamise.
    def LõpetaKirjutamine(self):
        self.pKast.kast.LõpetaKirjutamine()
        self.kKast.kast.LõpetaKirjutamine()
        self.aKast.kast.LõpetaKirjutamine()

    def LõpetaKõigiKirjutamine(self):
        pass


    def PaneValmis(self):
        kastideVahe = self.suurus[0] * 0.05
        kastiLaius = (self.suurus[0] - 2*kastideVahe)/3
        asuky = self.asukoht[1]

        # Päevakast
        asukx = self.asukoht[0] + kastiLaius/2
        self.pKast.MääraAsukoht((asukx, asuky))
        self.pKast.MääraSuurus((kastiLaius,0))
        
        # Kuukast
        asukx = asukx + kastiLaius + kastideVahe
        self.kKast.MääraAsukoht((asukx, asuky))
        self.kKast.MääraSuurus((kastiLaius,0))
        
        # Aastakast
        asukx = asukx + kastiLaius + kastideVahe
        self.aKast.MääraAsukoht((asukx, asuky))
        self.aKast.MääraSuurus((kastiLaius,0))

    def Joonista(self):
        self.pKast.Joonista()
        self.kKast.Joonista()
        self.aKast.Joonista()
     
    
    # See funktsioon tagastab None, kui ei ole piisavalt andmeid v on valed sisestused selleks, et võimalikku kuupäeva koostada. Tagastab Kuupäeva objketi, kui sisestustest saab teha kuupäeva.
    def VõtaKuupäev(self):
        if self.pKast.VõtaVeaTeade() == False:
            return None
        päev = int(self.pKast.VõtaTekst())
        
        if self.kKast.VõtaVeaTeade() == False:
            return None
        kuu = int(self.kKast.VõtaTekst())
        
        if self.aKast.VõtaVeaTeade() == False:
            return None
        aasta = int(self.aKast.VõtaTekst())
        
        kp = Kuupäev(päev, kuu, aasta)
        if kp.KasVõimalik() == False:
            return None
        
        return kp
            
    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        
    def MääraSuurus(self, suurus):
        self.suurus = suurus
        
    def VõtaSuurus(self):
        suurx = self.suurus[0]
        suury = max(self.pKast.VõtaSuurus()[1], self.kKast.VõtaSuurus()[1], self.aKast.VõtaSuurus()[1])
        return (suurx, suury)



class KellaajaKüsija:
    def __init__(self, olek, pind):
        # Tavalised omadused
        self.olek = olek
        self.pind = pind
        self.asukoht = (0,0)
        self.suurus = (300,300)
        
        # Alamobjektid
        self.tunniKast = SelgitavTekstikast(olek, pind)
        def tNupuF():
            self.LõpetaKõigiKirjutamine()
            self.tunniKast.kast.AlustaKirjutamist()
        self.tunniKast.MääraNupuF(tNupuF)
        self.tunniKast.tekst.MääraRidadeArv(1)
        self.tunniKast.MääraSõnum("Tund:")
        self.tunniKast.MääraKeskeleJoondus(True)
        self.tunniKast.MääraSelgitusKastiSees(True)
        
        self.minutiKast = SelgitavTekstikast(olek, pind)
        def mNupuF():
            self.LõpetaKõigiKirjutamine()
            self.minutiKast.kast.AlustaKirjutamist()
        self.minutiKast.MääraNupuF(mNupuF)
        self.minutiKast.tekst.MääraRidadeArv(1)
        self.minutiKast.MääraSõnum("Minut:")
        self.minutiKast.MääraKeskeleJoondus(True)
        self.minutiKast.MääraSelgitusKastiSees(True)

    # Määratakse ülemobjektis sellele klassile ja ülemobjekt kasutab sell koostamisel selle klassi LõpetaKirjutamine funktsiooni.
    def LõpetaKõigiKirjutamine(self): pass
    
    def LõpetaKirjutamine(self):
        self.tunniKast.kast.LõpetaKirjutamine()
        self.minutiKast.kast.LõpetaKirjutamine()

    def PaneValmis(self):
        # Neid väärtusi kasutavad mõlemad kastid.
        kastideVahe = self.suurus[0] * 0.05
        kastiLaius = (self.suurus[0] - kastideVahe) / 2
        
        # Tunnikast
        asukx = self.asukoht[0] + kastiLaius / 2
        asuky = self.asukoht[1]
        self.tunniKast.MääraAsukoht((asukx, asuky))
        self.tunniKast.MääraSuurus((kastiLaius, 0))
        
        # Minutikast
        asukx = self.asukoht[0] + kastideVahe + 1.5*kastiLaius
        asuky = self.asukoht[1]
        self.minutiKast.MääraAsukoht((asukx, asuky))
        self.minutiKast.MääraSuurus((kastiLaius, 0))
        
    def Joonista(self):
        self.tunniKast.Joonista()
        self.minutiKast.Joonista()
        
    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        
    def MääraSuurus(self, suurus):
        self.suurus = suurus
        
        
