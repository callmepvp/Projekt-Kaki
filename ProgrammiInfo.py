import os
import json
from Programmiolek import *
from Klassid.Sündmus import *

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
        "hoverTooniKordaja" : 0.8,
        
        "LisaSündmusNupuVärv" : (158, 240, 26, 255),
        "LisaSündmusNupuPlussiAluneVärv" : (40,40,40,255),

        "suureNupuTekstiSuurus" : 14,
        
        "suureNupuNurgaRaadius" : 20,

        "sündmuseLisamiseNurgaRaadius" : 30,

        "tekstikastiHelendavVärv": (140,140,140,255),
        "tekstikastiTavalineVärv" : (100,100,100,255),
        "tekstikastiVajutatudVärv" : (80,80,80,255),
        "tekstikastiRaamiLaius" : 2,
        "tekstikastiÜlemineServTekstist" : 15,
        "tekstikastiAlumineServTekstist" : 12,
        "tekstikastiKüljedTekstist" : 5,
        "tekstikastiReavahe" : 20,
        "tekstikastiSelgitusKastist" : 10,
        "tekstikastiSelgituseReavahe" : 10,

        "detailsemaVaateTaustaVärv" : (176, 176, 176, 255),
        "sündmuseLisamiseInfoKirjaSuurus" : 16,
        "sündmuseLisamiseHeledamaTaustaVärv" : (235,235,235,255),
        "sündmuseLisamiseHeledamaTaustaVahe" : 10,

        "DetailsemaVaateVäliPealkirjast" : 40,
        "DetailsemaVaateHeledamVärv" : (230, 230, 230, 255),
        "DetailsemaVaateVälistaustaLaius" : 15,
        "InfoVäljadeReaVahe" : 30

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

def VõtaInfoJaAnnaVäärtused(Olek: "ProgrammiOlek") -> None:
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

    #Sündmuste lisamine failist
    for key, value in programmiInfo["sündmused"].items():
        kuupäev = Kuupäev(value['alguskuupäev']['päev'], value['alguskuupäev']['kuu'], value['alguskuupäev']['aasta'])
        sündmus = Sündmus(value['nimi'], kuupäev, value['id'])
        sündmus.MääraLõppKell(value['lõppaeg']['tund'], value['lõppaeg']['minut'])

        Olek.sündmusteNimekiri.append(sündmus)

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

def SalvestaOlek(Olek):
    with open(dataFileDirectory, encoding="utf-8") as fail:
        programmiInfo = json.load(fail)

    failiSündmused = programmiInfo.get('sündmused', {})
    olemasolevadSündmused = Olek.sündmusteNimekiri #Sündmuste list

    #Tee list kõikidest sündmuste sõnastikest
    sündmusteSõnastikud = [sündmus.KonverteeriSõnastikuks() for sündmus in olemasolevadSündmused]
    for sündmus in sündmusteSõnastikud:
        if str(sündmus['id']) not in failiSündmused:
            print(f"Salvestan sündmuse ID'ga {sündmus['id']}")
            failiSündmused[sündmus['id']] = sündmus

    #kontrolli eemaldatud sündmusi
    olemasolevadID = set()
    kõikID = set()
    for k, v in failiSündmused.items():
        for sündmus in sündmusteSõnastikud:
            if str(k) == str(sündmus['id']):
                olemasolevadID.add(k)
                break

        kõikID.add(k)
        
    sündmusedVajaEemaldada = kõikID - olemasolevadID
    if len(olemasolevadID) != len(failiSündmused):

        #on toimunud sündmuste eemaldamine ning peab midagi failis muutma
        for el in sündmusedVajaEemaldada:
            del failiSündmused[el]

    programmiInfo['sündmused'] = failiSündmused

    with open(dataFileDirectory, "w", encoding="utf-8") as fail:
        json.dump(programmiInfo, fail, indent=indent, ensure_ascii=False)