#Panen siia praegu mingisuguse leet-code moodi asja, kuid enam-vähem see, mis sul mõttes oli.

class SündmusteNimekiri:

    def __init__(self, nimekiri):
        self.nimekiri = nimekiri #Master sündmuste nimekiri (?)

    def võtaSündmusedPäeval():
        pass

    def võtaSündmusedKuul():
        pass

    #def võtaSündmusedAastal():
        #pass (?)

    def võtaSündmusedPärastPäeva():
        pass

    def võtaSündmusedEnnePäeva():
        pass


    def võtaKestvusegaSündmus():
        pass

    def võtaNädalasedSündmused():
        pass


class Sündmus:
    # Kuupäevi käsitletakse 3-liikmelise tuplina, mis on järgmisel kujul (p, k, a),
    # kus p tähistab päeva arvu, k kuude arvu ja a aasta arvu.
    def __init__(self, nimi, kuupäev):
        self.nimi = nimi
        self.kuupäev = kuupäev

