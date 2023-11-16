import os
import json
from Programmiolek import *
from Sündmus import *

defaultDataBody = {
    "programmiInfo" : {
        "ruutudeTaustaLaius" : 0.8,
        "ruutudeTaustaNurgaÜmardus" : 10,

        "pvPealkKpSuurus" : 30, 
        "pvPealkAastaSuurus" : 10,
        "kuupäevaFondiNimi" : "Gogh-ExtraBold.ttf",
        "sündmuseFondiNimi" : "Gidole-Regular.ttf",

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

        "sündmuseRidadeVahe" : 30,

        "sündmuseReaTekstiJaKellaVahe" : 20,
        "sündmuseReadKuupäevast" : 30,

        "päevaruuduMinLaius" : 200,
        "päevaruutudeTaustaJaRuutudeVahe" : 20,

        "päevaruutudeVahe" : 10,
        "päevaruuduKõrgus" : 100,

        "päevaruutudeTaustaVärv" : (220,220,220,255),
        "päevaruutudeTaustaNurgaÜmardus" : 20,
        
        "LisaSündmusNupuVärv" : (255, 51, 102, 255),
        "LisaSündmusNupuPlussiAluneVärv" : (40,40,40,255),

        "suureNupuTekstiSuurus" : 30
    },

    "fondiTüübid" : {
        "päevaruuduPealkKpPygFont" : "pvPealkKpSuurus",
        "päevaruuduPealkAastaPygFont" : "pvPealkAastaSuurus",
        "sündmuseReaKirjaFont" : "sündmuseReaKirjaSuurus",
        "sündmuseReaAjaFont" : "sündmuseReaAjaSuurus",
        "suureNupuTekstiPygFont" : "suureNupuTekstiSuurus"
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
        if isinstance(value, list):
            #Kontrollib kas antud väärtus on list, mille ta peaks tegema ennikuks tagasi
            setattr(Olek, key, tuple(value))
        else:
            #Kui väärtus ei ole list
            setattr(Olek, key, value)

    #Paneb kõik fondid paika
    setattr(Olek, 'kuupäevaFondiPath', os.path.join("Fondid", getattr(Olek, 'kuupäevaFondiNimi')))
    setattr(Olek, 'sündmuseFondiPath', os.path.join("Fondid", getattr(Olek, 'sündmuseFondiNimi')))

    kuupäevaFondiVäärtus = getattr(Olek, 'kuupäevaFondiPath')
    sündmuseFondiVäärtus = getattr(Olek, 'sündmuseFondiPath')

    for item in programmiInfo["fondiTüübid"]:
        suuruseVäärtus = getattr(Olek, programmiInfo["fondiTüübid"][item])
        if item == "sündmuseReaKirjaFont":
            setattr(Olek, item, pygame.font.Font(sündmuseFondiVäärtus, suuruseVäärtus))
        else:
            setattr(Olek, item, pygame.font.Font(kuupäevaFondiVäärtus, suuruseVäärtus))

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

#* Loo igale sündmusele unikaalne ID
def SalvestaOlek(Olek):
    with open(dataFileDirectory, encoding="utf-8") as fail:
        programmiInfo = json.load(fail)

    failiSündmused = programmiInfo.get('sündmused', {})
    olemasolevadSündmused = Olek.sündmusteNimekiri #Sündmuste list

    #Tee list kõikidest sündmuste sõnastikest
    sündmusteSõnastikud = [sündmus.KonverteeriSõnastikuks() for sündmus in olemasolevadSündmused]
    for sündmus in sündmusteSõnastikud:
        failiSündmused[sündmus['nimi']] = sündmus

    programmiInfo['sündmused'] = failiSündmused

    with open(dataFileDirectory, "w", encoding="utf-8") as fail:
        json.dump(programmiInfo, fail, indent=indent, ensure_ascii=False)