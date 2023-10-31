# Selle klassi mõte on hoida endas kuupäeva ning väljastada kuupäeva kohta käivat vajalikku infot nt mis nädalapäev vastab sellele kuupäevale, kas aasta on liigaasta, kas kuu, päeva ja aasta numbrid üldse vastavad päris kuupäevale jms.

# Selles klassis on meetod kontrollimaks, kas kuupäev on võimalik, aga see ei tegele sellega, et õiget kuupäeva kasutajalt välja pinnida. Inputi võtmisega tegeletakse kuskil mujal.
import math

class Kuupäev:
    def __init__(self, päev, kuu, aasta):
        self.kuu = kuu
        self.päev = päev
        self.aasta = aasta


    def KasLiigaasta(self):
        if self.aasta % 4 == 0:
            if self.aasta % 100 == 0:
                if self.aasta % 400 == 0:
                    return True
                return False
            return True
        return False


    def KasVõimalik(self):
        kuudePikkused = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.aasta < 1800:
            return False
        if self.kuu < 1 or self.kuu > 12:
            return False
        if self.päev < 1:
            return False
        if self.kuu == 2 and self.KasLiigaasta() and self.päev > 29:
            return False
        if self.päev > kuudePikkused[self.kuu]:
            return False
        return True
        

    def VõtaKuupäev(self):
        return (self.päev, self.kuu, self.aasta)


    # See on crazy meetod. Väljastab numbri 1-7 vastavalt esmaspäevast pühapäevani
    def VõtaNädalaPäev(self):
        y = self.aasta
        m = self.kuu
        d = self.päev
        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        if m < 3:
            y -= 1
        return math.floor((y + y/4 - y/100 + y/400 + t[m-1] + d-1) % 7)+1


    def MuudaKuupäeva(self, päev, kuu, aasta):
        self.kuu = kuu
        self.päev = päev
        self.aasta = aasta