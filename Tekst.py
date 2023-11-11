import pygame
import os
from itertools import chain


# Ingliskeelne kood copy pastetud kusagilt lehelt, aga need funktsioonid teevad täpselt seda, mida vaja. Jagab antud teksti (stringi) tükkideks nii, et valitud fondi korral ei ületaks ükski tükk kindlat valitud laiust pikslites. Lühidalt jagab teksti tükkideks, et iga tüki saaks eraldi reale renderdada ja kõik oleksid roughly reapikkused.
"""
def truncline(text, font, maxwidth):
    real=len(text)       
    stext=text           
    l=font.size(text)[0]
    cut=0
    a=0                  
    done=1
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
    """ """returns text taking new lines into account."""
"""
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)

"""
# Funktsioon võtab sisse teksti, pikkuse pikslites ja pygame fonti objekti.
# Funktsioon tagastab esialgse teksti kahe tekstilise tuplena, millest esimene osa on nii pikk, et mahuks täpselt antud pikkusesse ja teine osa on kõik ülejäänud tekst.
def EraldaSobivaPikkusegaTekst(algtekst, sobivPikkus, fontObject:pygame.font.Font):
    kasvatatav = ""
    for i in algtekst:
        kasvatatav += i
        laius = fontObject.size(kasvatatav)[0]
        if laius > sobivPikkus:
            return (kasvatatav[:-1], algtekst[len(kasvatatav):])
    return (kasvatatav,"")



class Tekst:

    def __init__(self, pind, tekst, pygFont, värv=(255,0,0), asuk=(0,0)):
        self.pygFont = pygFont
        self.pind = pind
        self.asuk = asuk
        self.tekst = tekst
        self.värv = värv
    
    
    def Joonista(self):
        suurtäheKõrgus = self.pygFont.get_ascent()
        
        # Oke, see on scuffed ja töötab kindlalt ainult selle fondiga. 0.22 on silma järgi valitud, aga see arv aitab teha nii, et tekst joonistuks valitud kohta täpselt nii, et väiketähe kõrguse keskkoht oleks soovitud kõrgusel. Keskkoht selle pärast, et ss on bullet pointe lihtsam joondada. Seda peaks vist täiendama, kui on vaja kirjutada mitmerealine tekst. Scuffed on veel see, et height on fontide terminoloogias väiketähe kõrgus, aga siin imo on vahemik nt j tähe langusest l tähe tõusuni, seega u 2x väiketähe kõrgus.
        poolVäiketäheKõrgus = self.pygFont.get_height()*0.22
        
        tekstiAsuk = (self.asuk[0], self.asuk[1]-suurtäheKõrgus + poolVäiketäheKõrgus)

        img = self.pygFont.render(self.tekst, True, self.värv)
        self.pind.blit(img, tekstiAsuk)


    def MääraAsukoht(self, asuk):
        self.asuk = asuk

    def MääraTekst(self, tekst):
        self.tekst = tekst




class MitmeReaTekst:
    pass
            
        
