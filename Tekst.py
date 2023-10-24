import pygame
import pygame.freetype

class Tekst:

    def __init__(self, pind, tekst, font="CORBEL.TTF", värv=(255,0,0), asuk=(0,0), suurus=60):
        self.font = pygame.font.SysFont(font, suurus)
        self.pind = pind
        self.asuk = asuk
        self.img = self.font.render(tekst, True, värv)
        self.värv = värv
    
    
    def Joonista(self):
        suurtäheKõrgus = self.font.get_ascent()
        
        # Oke, see on scuffed ja töötab kindlalt ainult selle fondiga. 0.34 on silma järgi valitud, aga see arv aitab teha nii, et tekst joonistuks valitud kohta täpselt nii, et väiketähe kõrguse keskkoht oleks soovitud kõrgusel. Keskkoht selle pärast, et ss on bullet pointe lihtsam joondada. Seda peaks vist täiendama, kui on vaja kirjutada mitmerealine tekst. Scuffed on veel see, et height on fontide terminoloogias väiketähe kõrgus, aga siin imo on vahemik nt j tähe langusest l tähe tõusuni, seega u 2x väiketähe kõrgus.
        poolVäiketäheKõrgus = self.font.get_height()*0.34
        

        tekstiAsuk = (self.asuk[0], self.asuk[1]-suurtäheKõrgus + poolVäiketäheKõrgus)

        self.pind.blit(self.img, tekstiAsuk)
