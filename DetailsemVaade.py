from Päev import Päev

class DetailsemVaade:
    def __init__(self, päevaObjekt: "Päev") -> None:
        self.päevaObjekt = päevaObjekt
        self.asukoht = (0, 0)
        self.suurus = (400, 200)

    def MääraSuurus(self, suurus):
        self.suurus = suurus

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht

    def Joonista(self):
        pass