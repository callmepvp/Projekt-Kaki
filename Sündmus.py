from Kuupäev import Kuupäev, Kellaaeg
import json


# Sündmusel põhineb kõik selles programmis. See objekt peab olema piisavalt paindlik, et saada olla ühekordne Kuupäeva sündmus või olla igal kolmapäeval ja esmaspäeval kl 18 korduv sündmus või näiteks sündmus algusega kl 17 ja lõpuga kl 19.

# Kui objekti muutujal mingit väärtust ei ole, siis on selle väärtuseks None. Näiteks, kui pole alguskellaaega, ss on algusKella väärtus None.
class Sündmus:
    
    # Ürituse pealkiri on string ja kuupäev on Kuupäeva objekt.
    def __init__(self, nimi, kuupäev:Kuupäev, id):

        self.id = id

        self.nimi = nimi

        # Need on sündmuseolekud
        # 0. ainult alguskuupäev
        # 1. alguskuupäev ja alguskell
        # 2. alguskuupäev ja lõppkuupäev
        # 3. Alguskuupäev, alguskell, lõppkuupäev
        # 4. alguskuupäev, lõppkuupäev, lõppkell
        # 5. Alguskuupäev, lõppkuupäev, alguskell, lõppkell
        self.ajaTüüp = 0

        self.alguskuupäev = kuupäev
        self.lõppkuupäev = Kuupäev(12, 23, 1994)
        self.algusaeg = Kellaaeg(18,34)
        self.lõppaeg = Kellaaeg(19, 55)

        

        # Kordumise tüüp on number 0-2, erinevate tähendustega.
        # 0. kordumist pole, kordumist kirjdavaid väärtusi ei vaadata.
        # 1. Kordumine iga aasta kindlal kuupäeval
        # 2. kordumine iga kuu kindlal päeval
        # 3. kordumine igal mingil nädalapäeval
        # 4. kordumine iga ajapikkuse tagant
        self.kordumiseTüüp = 0
        self.kordumiseAjavahemik = 0 #Aeg()

        
        


    def VõtaNimi(self):
        return self.nimi

    def VõtaKuupäev(self):
        return self.algusKuupäev.VõtaKuupäev()

    def MääraLõppKell(self, tund, minut):
        self.lõppKell = Kellaaeg(tund, minut)

    def KasAlgabPäeval(self, kuupäev:"Kuupäev"):
        if self.alguskuupäev.KasOnSama(kuupäev):
            return True
        return False

    def KasOnPäeval(self, kuupäev:Kuupäev):
        # See funktsioon päeab väljastama True, kui sündmus on parameetriks oleval päeval. See tähendab järgmist:

        # Kui sündmus pole korduv, on asi igatahes lihtne:
            # Kui on ajatüüp 0 v 1 st sündmus toimub ühel päeval
                # Kui on samal päeval uuritavaga, ss True
            # Kui on ajatüüp 2, 3, 4 v 5 st sündmus toimub vahemikus
                # Kui uuritav kuupäev on alguspäeval v lõpppäeval v nende kahe vahel, ss True
        # Kui sündmus on kordusega, ss on pmst esimene juhtum, ainult et tuleb kontrollida kõiki vahemikke v päevi, millal see sündmus toimub ja ühegi kokkulangevuse puhul returnida True.


        # Prg kõige kõige lollimalt lihtsam versioon.
        if self.alguskuupäev.KasOnSama(kuupäev):
            return True
        return False
    


    #Meetod, mis tagastab kõik sündmuse parameetrid json-loetavas sõnastikus, kusjuures kõik parameetrid, mille väärtuseks on teine objekt, on tagastatud teisejärgulise sõnastikuna
    def KonverteeriSõnastikuks(self):
        väljund = {
            "nimi" : self.nimi,
            "ajaTüüp" : self.ajaTüüp,
            "id" : self.id,
            
            "alguskuupäev" : self.TagastaOsaObjektid(self.alguskuupäev) if self.alguskuupäev else None,
            "lõppkuupäev" : self.TagastaOsaObjektid(self.lõppkuupäev) if self.lõppkuupäev else None,
            "algusaeg" : self.TagastaOsaObjektid(self.algusaeg) if self.algusaeg else None,
            "lõppaeg" : self.TagastaOsaObjektid(self.lõppaeg) if self.lõppaeg else None,

            "kordumiseTüüp" : self.kordumiseTüüp,
            "kordumiseAjavahemik" : self.kordumiseAjavahemik
        }

        return väljund
    
    #Leiab ja tagastab kõik väärtused, mis on osaobjekti sees
    def TagastaOsaObjektid(self, obj):
        if obj is None:
            return None
        
        elif isinstance(obj, list):
            return [self.TagastaOsaObjektid(item) for item in obj]
        
        elif isinstance(obj, dict):
            return {key: self.TagastaOsaObjektid(value) for key, value in obj.items()}
        
        elif hasattr(obj, '__dict__'):
            return {key: self.TagastaOsaObjektid(value) for key, value in obj.__dict__.items()}
        
        else:
            return obj

