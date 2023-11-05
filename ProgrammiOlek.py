import pygame
import os

#Klass, mis hoiab neid v��rtusi, mis loetakse failist ja kirjeldavad programmi v�limust. Selles klassis olevad numbrid m��ravad eri kohtades olevate kirjade suurused, v�rvid, kaugused p�evaruutude vahel, programmi taustaks oleva pildi, dropshadowi laiuse, rounded cornerite raadiused � k�ikv�imaliku programmi kirjeldava. Iga objekti k�sib luues programmiolekut parameetriks. See tundub mulle olevat ainus viis, kuidas mitte hard codeda asju.
class ProgrammiOlek:
    def __init__(self):
        pygame.init()
        
        # P�evaruutudel on taga taust, mis aitab ruute eraldada k�ige taga olevast pildist. See mutuja kirjeldab selle tausta laiust aknas, kus 0 on olematu laius, 0.8 on 80% ekraani laiusest ja 1 on terve ekraani laius.
        self.ruutudeTaustaLaius = 0.8

        # P�evaruutude tausta �mardatud nurkade raadius pikslites. Hiljem vb teeb selle teguriks akna laiusest v k�rgusest v m�lemast, aga ei viitsi prg m�elda.
        self.ruutudeTaustaNurga�mardus = 10
        
        # Pygame fondiobjektid eri kohtade jaoks. Ma arvan, et on parem, kui need on salvestatud programmiolekusse, mitte ei hakata v�imalik et iga kaader looma seda fondiobjekti algusest peale.
        self.font = os.path.join("Fondid", "Gogh-ExtraBold.ttf")
        self.p�evaruuduTekstiPygFont = pygame.font.Font(self.font, 20)
        self.p�evaruuduPealkirjaPygFont = pygame.font.Font(self.font, 30)

        # Teksti v�rv p�evaruutudes
        self.ruuduTekstiV�rv = (20, 20, 20)


    # Funktsioon, mis loeb faili ja selle p�hjal m��rab klassimuutujate v��rtusi. 
    def V�taOlekFailist():
        pass

    # Funktsioon, mis salvestab klassimuutujad faili, et neid sealt j�rgmine kord uuesti sisse lugeda.
    def SalvestaOlek(self):
        pass