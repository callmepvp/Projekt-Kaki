import pygame
import os
from typing import List

#from Klassid.Nupp import NupuAlus

#Klass, mis hoiab neid väärtusi, mis loetakse failist ja kirjeldavad programmi välimust. Selles klassis olevad numbrid määravad eri kohtades olevate kirjade suurused, värvid, kaugused päevaruutude vahel, programmi taustaks oleva pildi, dropshadowi laiuse, rounded cornerite raadiused – kõikvõimaliku programmi kirjeldava. Iga objekti küsib luues programmiolekut parameetriks. See tundub mulle olevat ainus viis, kuidas mitte hard codeda asju.
class ProgrammiOlek:
    def __init__(self):
        pygame.init()

        # See nimekiri on master sündmustenimekiri ja selle sisu tuleb programmi lõpus salvestada ja igal alustamisel sellesse nimekirja lugeda. Pärast alustamist läheb see nimekiri
        self.sündmusteNimekiri = []
        
        # Päevaruutudel on taga taust, mis aitab ruute eraldada kõige taga olevast pildist. See mutuja kirjeldab selle tausta laiust aknas, kus 0 on olematu laius, 0.8 on 80% ekraani laiusest ja 1 on terve ekraani laius.
        self.ruutudeTaustaLaius = 0.8

        # Päevaruutude tausta ümardatud nurkade raadius pikslites. Hiljem vb teeb selle teguriks akna laiusest v kõrgusest v mõlemast, aga ei viitsi prg mõelda.
        self.ruutudeTaustaNurgaÜmardus = 10
        
        #Fondi suurused
        self.pvPealkKpSuurus = 30
        self.pvPealkAastaSuurus = 10

        # Pygame fondiobjektid eri kohtade jaoks. Ma arvan, et on parem, kui need on salvestatud programmiolekusse, mitte ei hakata võimalik et iga kaader looma seda fondiobjekti algusest peale.
        self.kuupäevaFondiNimi = "Gogh-ExtraBold.ttf"
        self.kuupäevaFondiPath = os.path.join("Fondid", self.kuupäevaFondiNimi)

        self.sündmuseFondiNimi = "Gidole-Regular.ttf"
        self.sündmuseFondiPath = os.path.join("Fondid", self.sündmuseFondiNimi)

        #Päevaruudu pealkirja pygame fondid.
        self.päevaruuduPealkKpPygFont = pygame.font.Font(self.kuupäevaFondiPath, self.pvPealkKpSuurus)
        self.päevaruuduPealkAastaPygFont = pygame.font.Font(self.kuupäevaFondiPath, self.pvPealkAastaSuurus)

        # Teksti värv päevaruutudes
        self.ruuduTekstiVärv = (30, 30, 30)

        # Väikese vahe suurus, mis on päevaruudu pealkirjas suurelt kirjutatud kuupäeva ja väikselt kirjutatud aasta vahel.
        self.päevaruuduPealkPäevaAastaVahe = 10

        # Päevaruudu taustaks oleva ristküliku värv. Hiljem vb lisab transparency efecti ja ss see asi vb muutub kuidagi.
        self.päevaruuduVärv = (100,100,100, 255)
        #print(self.päevaruuduVärv)
        # Päevaruudu pealkirja asukoht päevaruudu suhtes
        self.päevaruuduPealkKaugusÜlaservast = 20
        self.päevaruuduPealkKaugusVasakult = 5

        #Fondi suurused
        self.sündmuseReaKirjaSuurus = 20
        self.sündmuseReaAjaSuurus = 10
        
        # Päevaruudus olevate sündmuseridade fondid sündmuse pealkirja jaoks ja rea lõpus oleva kellaaja jaoks.
        self.sündmuseReaKirjaFont = pygame.font.Font(self.sündmuseFondiPath, self.sündmuseReaKirjaSuurus)
        self.sündmuseReaAjaFont = pygame.font.Font(self.kuupäevaFondiPath, self.sündmuseReaAjaSuurus)

        # Sündmuserea teksti ja loetelutäpi vahel oleva vahe suurus
        self.sündmuseReaTäpiVahe = 15

        # Sündmusrea teksti ees oleva loetelupunkti raadius
        self.sündmuseReaTäpiRaadius = 4
        
        # Sündmuserea kaugus päevaruudu vasakust servast
        self.sündmuseRidaVasakult = 10
        # sündmuseRea kaugus päevaruudu paremast servast. Kui see väärtus koos vasakpoolse kaugusega lahutada päevaruudu laiusest, saab sündmuserea laiuse.
        self.sündmuseRidaParemalt = 10

        # Sündmusteridade vahe suurus. Kui palju piksleid on üksteise all olevate sündmuseridade keskkohtade vahel.
        self.sündmuseRidadeVahe = 30

        # See kui palju on ühe sündmuserea ridade vahe. Mõte on, et kui päevaruut läheb kitsaks, ss ei ole normaalne piirata sündmuserea teksti ühele reale, sest sinna mahub nii vähe, et on loetamatu. Ss läheb rida mitmele reale ja see suurus on nende ridade vahe.
        self.sündmuseReaReavahe = 20

        # See, kui mitu rida võib ühe sündmuse tekst päevaruudus võtta.
        self.sündmuseReaRidu = 3

        # Selle vahe suurus, mis on sündmuserea teksti ja sellele järgneva kellaaja vahel.
        self.sündmuseReaTekstiJaKellaVahe = 25

        # Selle vahe suurus, mis on päevaruudus kõige ülemise sündmuse ja kuupäeva vahel, Täpsemalt kuupäeva keskkoha ja sündmuse keskkoha vahel.
        self.sündmuseReadKuupäevast = 20

        # Päevaruutude minimaalne laius. Kui akna suuruse vähendamisel läheks reas olevate päevaruutude laius selelst väiksemaks, läheb reas viimane ruut uuele reale, seega eelmisel real on rohkem ruumi ja ruudud ei pea olema väiksemad kui min laius.
        self.päevaruuduMinLaius = 200

        # Päevaruutude taga on taustaks suur ristkülik, mis aitab ruute kõige taga olevast pildist paremini eraldada. See vahe on päevaruutudel tausta servast. Kaugus ülevalt, alt, paremalt ja vasakult on kõik sama.
        self.päevaruutudeTaustaJaRuutudeVahe = 20

        # See vahe on päevaruutude ruudustikus kahe kõrvuti v üksteise all oleva ruudu vahel.
        self.päevaruutudeVahe = 10

        # Päevaruutude kõrgus. Erinevalt laiusest see ei muutu akna suuruse muutmisel. 
        self.päevaruuduKõrgus = 100

        self.päevaruutudeTaustaVärv = (220,220,220,255)

        self.päevaruutudeTaustaNurgaÜmardus = 20

        self.hoverTooniKordaja = 1.1
       
        self.suureNupuTekstiSuurus = 10
        self.suureNupuTekstiPygFont = pygame.font.Font(self.sündmuseFondiPath, self.suureNupuTekstiSuurus)

        self.LisaSündmusNupuVärv = (255, 51, 102, 255)
        self.LisaSündmusNupuPlussiAluneVärv = (40,40,40,255)
        
        self.suureNupuNurgaRaadius = 20
        
        self.pygameEvents = None
        
        # See muutuja on Päevaobjekt siis, kui on klõpsatud mingi päevaruudu peale ja seega peaks olema lahti selle päeva detailsem vaade. Muutuja on None, kui ei pea olema avatud ühegi päeva vaade.
        self.TäpsemaVaatePäev = None
        
        # See muutuja on True siis, kui peab olema lahti sünmduse lisamise aken. False siis, kui aken ei pea avatud olema. Suht elementaarne.
        self.SündmuseLisamine = False
        
        # See on sündmuse lisamise valikuakna nurgaraadiused.
        self.sündmuseLisamiseNurgaRaadius = 30
        
        # See o sündmuse lisamise valikuakna tausta värv
        self.sündmuseLisamiseTaustaVärv = (200,200,200,255)
        
        self.nuppudePrioriteedid = {
            "taust": 0,
            "päevaruut": 1,
            "sündmuse lisamise nupp": 2,
            "detailsem vaade" : 3,
            "sündmuse lisamise aken" : 4}

        self.aktiivsedNupud = set()
