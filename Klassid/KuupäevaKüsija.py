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
            self.LõpetaKirjutamine()
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
            self.LõpetaKirjutamine()
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
            self.LõpetaKirjutamine()
            self.aKast.kast.AlustaKirjutamist()
        self.aKast.MääraNupuF(aNupuF)
        self.aKast.tekst.MääraRidadeArv(1)
        self.aKast.MääraVeaKontrolliFunktsioon(intKontroll)
        self.aKast.MääraSõnum("Aasta:")
        self.aKast.MääraKeskeleJoondus(True)
        self.aKast.MääraSelgitusKastiSees(True)
        
    def PaneValmis(self):
        kastideVahe = self.suurus[0] * 0.05
        kastiLaius = (self.suurus[0] - 2*kastideVahe)/3
        asuky = self.asukoht[1]

        # Päevakast
        asukx = self.asukoht[0] + kastiLaius
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
        
    def LõpetaKirjutamine(self):
        self.pKast.kast.LõpetaKirjutamine()
        self.kKast.kast.LõpetaKirjutamine()
        self.aKast.kast.LõpetaKirjutamine()

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