import os
import json

"""
näidis json file'ist, mis salvestab informatsiooni.

Mõte on selles, et iga sündmus peaks salvestama kõik võimalikud väljad ära, st. et ta ei jätaks ühtegi välja tühjaks.
See on tehtav ka nii, et tal mitte-vajaminevad väljad on tühjad, kuid siis (potensiaalselt) võib tekkida probleeme, kui programm kogemata peaks indexima väärtust, mida tal pole.
See viskaks errori ning lihtsam oleks lihtsalt returnida tühi väärtus (None, 0, NaN).

{  
    "programmiInfo" : {
        "font": ""
    },
    
    "sündmused": {
        "teatrisseminek": {
            "algKuupäev": (),
            "lõppKuupäev": (),
            "korduvus": False,
            "korduvuseTüüp": "None",
            "algKell": (),
            "lõppKell": (),
            
            ...
            "muud vajalikud abi-informatsioon salvestajad" : 0
        },

        "surnuaia visiit": {
            ...

            "samad asjad"
        }
    }
}

Programm looks kohe esimese jooksutamisega faili (kutsuks cache'i uuendust kohe esimese pauguga)
Siis peamiselt programmi kinni pannes salvestab ta cache'i ära.
(See on parem nii teha, sest programmi töö jooksul on suhteliselt riskantne uuendada ühte ja sama data filei pärast igat actionit, sest me ei tea tegelikult kas ta suudab tohutult kiiresti igat infot ära salvestada)

"""

#Salvestamiseks
def SalvestaFaili():
    #salvestab alati cache faili data faili
    with open("./Data/cache.json", encoding="utf-8") as cache:
        tempData = cache.read()

    with open("./Data/data.json", "w", encoding="utf-8") as f:
        f.write(tempData)

    os.remove("./Data/cache.json") #removes the cache fail

def UuendaCache(cacheObject):
    with open("./Data/cache.json", "w", encoding="utf-8") as f:
        f.write(cacheObject)


#Laadimiseks
#Praegu on kaks andmetüüpi, mida saab indexida -> programmiInfo ja sündmused
def VõtaFailist(andmeteTüüp):
    with open("./Data/data.json", encoding="utf-8") as f:
        info = json.load(f)

    return info[andmeteTüüp]