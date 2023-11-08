import pygame
import os

#Klass, mis hoiab neid väärtusi, mis loetakse failist ja kirjeldavad programmi välimust. Selles klassis olevad numbrid määravad eri kohtades olevate kirjade suurused, värvid, kaugused päevaruutude vahel, programmi taustaks oleva pildi, dropshadowi laiuse, rounded cornerite raadiused – kõikvõimaliku programmi kirjeldava. Iga objekti küsib luues programmiolekut parameetriks. See tundub mulle olevat ainus viis, kuidas mitte hard codeda asju.
class ProgrammiOlek:
    def __init__(self):
        pygame.init()
        
        # Päevaruutudel on taga taust, mis aitab ruute eraldada kõige taga olevast pildist. See mutuja kirjeldab selle tausta laiust aknas, kus 0 on olematu laius, 0.8 on 80% ekraani laiusest ja 1 on terve ekraani laius.
        self.ruutudeTaustaLaius = 0.8

        # Päevaruutude tausta ümardatud nurkade raadius pikslites. Hiljem vb teeb selle teguriks akna laiusest v kõrgusest v mõlemast, aga ei viitsi prg mõelda.
        self.ruutudeTaustaNurgaÜmardus = 10
        
        # Pygame fondiobjektid eri kohtade jaoks. Ma arvan, et on parem, kui need on salvestatud programmiolekusse, mitte ei hakata võimalik et iga kaader looma seda fondiobjekti algusest peale.
        self.font = os.path.join("Fondid", "Gogh-ExtraBold.ttf")
        self.päevaruuduTekstiPygFont = pygame.font.Font(self.font, 20)
        self.päevaruuduPealkKpPygFont = pygame.font.Font(self.font, 30)
        self.päevaruuduPealkAastaPygFont = pygame.font.Font(self.font, 10)

        # Teksti värv päevaruutudes
        self.ruuduTekstiVärv = (30, 30, 30)

        # Väikese vahe suurus, mis on päevaruudu pealkirjas suurelt kirjutatud kuupäeva ja väikselt kirjutatud aasta vahel.
        self.päevaruuduPealkPäevaAastaVahe = 10

        # Päevaruudu taustaks oleva ristküliku värv. Hiljem vb lisab transparency efecti ja ss see asi vb muutub kuidagi.
        self.päevaruuduVärv = (235,235,235, 255)

        # Päevaruudu pealkirja asukoht päevaruudu suhtes
        self.päevaruuduPealkKaugusÜlaservast = 20
        self.päevaruuduPealkKaugusVasakult = 5

        # Päevaruudus olevate sündmuseridade fondid sündmuse pealkirja jaoks ja rea lõpus oleva kellaaja jaoks.
        self.sündmuseReaKirjaFont = pygame.font.Font(self.font, 20)
        self.sündmuseReaAjaFont = pygame.font.Font(self.font, 10)

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

        # Selle vahe suurus, mis on sündmuserea teksti ja sellele järgneva kellaaja vahel.
        self.sündmuseReaTekstiJaKellaVahe = 20

        # Selle vahe suurus, mis on päevaruudus kõige ülemise sündmuse ja kuupäeva vahel, Täpsemalt kuupäeva keskkoha ja sündmuse keskkoha vahel.
        self.sündmuseReadKuupäevast = 20



    # Funktsioon, mis loeb faili ja selle põhjal määrab klassimuutujate väärtusi. 
    def VõtaOlekFailist():
        pass

    # Funktsioon, mis salvestab klassimuutujad faili, et neid sealt järgmine kord uuesti sisse lugeda.
    def SalvestaOlek(self):
        pass