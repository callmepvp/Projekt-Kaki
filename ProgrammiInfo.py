import os
import json
from Programmiolek import *

defaultDataBody = {
    "programmiInfo" : {
        "ruutudeTaustaLaius" : 0.8,
        "ruutudeTaustaNurgaÜmardus" : 10,

        "pvPealkKpSuurus" : 30, 
        "pvPealkAastaSuurus" : 10,
        "fondiNimi" : "Gogh-ExtraBold.ttf",

        "ruuduTekstiVärv" : (30,30,30),

        "päevaruuduPealkPäevaAastaVahe" : 10,
        "päevaruuduVärv" : (235,235,235,255),

        "päevaruuduPealkKaugusÜlaservast" : 20,
        "päevaruuduPealkKaugusVasakult" : 5,

        "sündmuseReaKirjaSuurus" : 20,
        "sündmuseReaAjaSuurus" : 10,

        "sündmuseReaTäpiVahe" : 15,
        "sündmuseReaTäpiRaadius" : 4,

        "sündmuseRidaVasakult" : 10,
        "sündmuseRidaParemalt" : 10,

        "sündmuseRidadeVahe" : 100,

        "sündmuseReaTekstiJaKellaVahe" : 20,
        "sündmuseReadKuupäevast" : 20,

        "päevaruuduMinLaius" : 200,
        "päevaruutudeTaustaJaRuutudeVahe" : 20,

        "päevaruutudeVahe" : 10,
        "päevaruuduKõrgus" : 100,

        "päevaruutudeTaustaVärv" : (220,220,220,255),
        "päevaruutudeTaustaNurgaÜmardus" : 20
    },

    "fondiTüübid" : {
        "päevaruuduPealkKpPygFont" : "pvPealkKpSuurus",
        "päevaruuduPealkAastaPygFont" : "pvPealkAastaSuurus",
        "sündmuseReaKirjaFont" : "sündmuseReaKirjaSuurus",
        "sündmuseReaAjaFont" : "sündmuseReaAjaSuurus"
    },

    "sündmused" : {

    }
}

indent = 4 #json indent formatting

indexDirectory = os.path.dirname(__file__) #Python scripti relatiivne path
dataFileDirectory = os.path.join(indexDirectory, 'Data/data.json')

def VõtaInfoJaAnnaVäärtused(Olek: object) -> None:
    #Programm on varem käivitunud
    with open(dataFileDirectory, encoding="utf-8") as fail:
        programmiInfo = json.load(fail)

    #Paneb kõik parameetrid paika
    for key, value in programmiInfo["programmiInfo"].items():
        setattr(Olek, key, value)

    #Paneb kõik fondid paika
    setattr(Olek, 'font', os.path.join("Fondid", getattr(Olek, 'fondiNimi')))
    fondiVäärtus = getattr(Olek, 'font')
    for item in programmiInfo["fondiTüübid"]:
        suuruseVäärtus = getattr(Olek, programmiInfo["fondiTüübid"][item])
        setattr(Olek, item, pygame.font.Font(fondiVäärtus, suuruseVäärtus))

def VõtaOlek():
    Olek = ProgrammiOlek()

    #Võta info failist
    if os.path.isfile(dataFileDirectory):
        VõtaInfoJaAnnaVäärtused(Olek)

    else:
        #Programm ei ole varem käivitunud
        with open(dataFileDirectory, "w", encoding="utf-8") as fail:
            json.dump(defaultDataBody, fail, ensure_ascii=False, indent=indent)

        VõtaInfoJaAnnaVäärtused(Olek)

    return Olek

def SalvestaOlek(olek):
    pass