
from Kuupäev import Kuupäev, Kellaaeg
from typing import List
from Päev import Päev


#Panen siia praegu mingisuguse leet-code moodi asja, kuid enam-vähem see, mis sul mõttes oli.

class SündmusteNimekiri:
    
    def __init__(self, nimekiri):
        #Master sündmuste nimekiri
        self.nimekiri: List[Sündmus] = nimekiri

    def võtaSündmusedPäeval():


        pass


    def VõtaPäevadena(self):
        päevaNimek: List[Päev] = []

        for i in self.nimekiri:
            pass


    def võtaSündmusedKuul():
        pass

    #def võtaSündmusedAastal():
        #pass (?)

    def võtaSündmusedPärastPäeva():
        pass

    def võtaSündmusedEnnePäeva():
        pass


    def võtaKestvusegaSündmus():
        pass

    def võtaNädalasedSündmused():
        pass

    def VõtaSündmustegaKuupäevad(self):
        kuupäevad = []
        for i in self.nimekiri:
            kp = i.VõtaKuupäev()
            if kp not in kuupäevad:
                kuupäevad.append(kp)

        return kuupäevad


















"""class Sündmus:
    nimi
    algKuupäev
    lõppkuupäev
    algkell
    lõppkell

    kordumiseTüüp
    0: # ei ole korduvust
    1: # iga Kuupäev
    2: # iga aja tagant
    if kordumisetüüp == 0:
        pass
    elif kordumisetüüp == 1:
    kordumisTsükkel: päevadekogus

    tonificatiobiTüü:0, 1, 2
    pole notificationit
    abs kellaaeg
    aeg enne sündmust
        


    """