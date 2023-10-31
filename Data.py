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

indexDirectory = os.path.dirname(__file__) #Python scripti relatiivne path
dataDirectory = os.path.join(indexDirectory, 'Data/data.json')
cacheDirectory = os.path.join(indexDirectory, 'Data/cache.json')

#Salvestamiseks
def SalvestaFaili():
    #salvestab alati cache faili data faili
    #! tulevikus muuda salvestamine nii, et ta mitte ei fully kirjutaks üle, vaid vaataks, mis on muutunud ja asendaks ainult selle
    with open(cacheDirectory, encoding="utf-8") as cache:
        tempData = cache.read()

    with open(dataDirectory, "w", encoding="utf-8") as f:
        f.write(tempData)

    os.remove(cacheDirectory) #removes the cache fail

def SalvestaCache(cacheObject: str):
    with open(cacheDirectory, "w", encoding="utf-8") as f:
        f.write(cacheObject)


#Laadimiseks
def VõtaCache(andmeteTüüp: str):
    with open(cacheDirectory, encoding="utf-8") as f:
        info = json.load(f)

    return info[andmeteTüüp]

def VõtaData(andmeteTüüp: str):
    with open(dataDirectory, encoding="utf-8") as f:
        info = json.load(f)

    return info[andmeteTüüp]