from Kuupäev import Kuupäev
from typing import List
from Sündmus import Sündmus


# Päev on objekt milles on kuupäeva objekt ja sellel päeval olevad sündmused nimekirjas. Nende objekti nimekirja võtab sisse päevaruudustiku klass, et 
class Päev:
    def __init__(self, kuupäev:Kuupäev, sündmusteNimekiri:List[Sündmus]):
        self.kuupäev = kuupäev
        self.sündmusteNimekiri = sündmusteNimekiri

    def VõtaSündmused(self):
        return self.sündmusteNimekiri

    def VõtaKuupäev(self):
        return self.kuupäev