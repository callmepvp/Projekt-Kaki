import pygame
from itertools import chain

# Ingliskeelne kood copy pastetud kusagilt lehelt, aga need funktsioonid teevad täpselt seda, mida vaja. Jagab antud teksti (stringi) tükkideks nii, et valitud fondi korral ei ületaks ükski tükk kindlat valitud laiust pikslites. Lühidalt jagab teksti tükkideks, et iga tüki saaks eraldi reale renderdada ja kõik oleksid roughly reapikkused.

def truncline(text, font, maxwidth):
    real=len(text)       
    stext=text           
    l=font.size(text)[0]
    cut=0
    a=0                  
    done=1
    old = None
    while l > maxwidth:
        a=a+1
        n=text.rsplit(None, a)[0]
        if stext == n:
            cut += 1
            stext= n[:-cut]
        else:
            stext = n
        l=font.size(stext)[0]
        real=len(stext)               
        done=0                        
    return real, done, stext             
        
def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped

def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account.
    """
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)



class Tekst:

    def __init__(self, pind, tekst, font="CORBEL.TTF", värv=(255,0,0), asuk=(0,0), suurus=60):
        self.font = pygame.font.Font(font, suurus)
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

class MitmeReaTekst:

    def __init__(self, pind, tekst="Lorem Ipsum", reaLaius=400, font="CORBEL.TTF", värv=(255,0,0), asuk=(0,0), suurus=60, reavahe=50):
        self.font = font
        self.pygfont = pygame.font.Font(font, suurus)
        self.pind = pind
        self.asuk = asuk
        self.img = self.pygfont.render(tekst, True, värv)
        self.värv = värv
        self.tekst = tekst
        self.reaLaius = reaLaius
        self.reavahe = reavahe
        self.suurus = suurus
    
    
    def Joonista(self):
        read = wrap_multi_line(self.tekst, self.pygfont, self.reaLaius)

        mitmes = 0
        for i in read:
            print(self.font)
            reaAsukoht = (self.asuk[0], self.asuk[1] + self.reavahe*mitmes)
            rida = Tekst(self.pind, i, asuk=reaAsukoht, font=self.font, värv=self.värv, suurus=self.suurus)
            rida.Joonista()
            mitmes += 1
            
        
