class SündmuseRida:
    def __init__(self, pind, sündmus, asukoht):
        self.sündmus = sündmus
        self.pind = pind
        self.asukoht = asukoht

    def Joonista(self):
        
        # Täpp teksti ees.
        pygame.draw.circle(self.pind, (10, 10, 10), self.asukoht, 5.0)

        #Sündmuse nimi
        tekstiAsuk = (self.asukoht[0] + 20, self.asukoht[1])
        pealkiri = Tekst(self.pind, "Lamp sündmuserida.", asuk=tekstiAsuk, värv=(10,10,10), suurus=40)
        pealkiri.Joonista()

        #Sündmuse kellaaeg väiksemalt.
        #Siia on kellaaja asukoht hard codetud. Kui pealkirja tekst läheb pikemaks, ss see hakkab kellaajaga kattuma. Tuleb teha nii, et pealkirja tekst kas hääbuks nähtamatuks enne kellaaega v läheks teisele reale. Esimene on lihtsam ma arvan, aga ma ei tea, kuidas sedagi teha.
        
        pealkiri = Tekst(self.pind, "19.30", asuk=(self.asukoht[0]+400, self.asukoht[1]), värv=(10,10,10), suurus=30)
        pealkiri.Joonista()

        self.sündmus.VõtaNimi()
        self.sündmus.VõtaAlgusKell()
        self.sündmus.VõtaLõppkell()