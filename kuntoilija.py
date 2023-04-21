# KUNTOILIJAN TIEDOT OLIO OHJELMOINIA

# Kirjastot ja moduulit
import fitness

# Luokkamääritykset
# Kuntoilija luokka Yliluokka JunioriKuntoilijalle
class Kuntoilija:
    """Luokka kuntoilijan tietoja varten
    """
    # Olionmuodostin eli konstruktori
    def __init__(self, nimi, pituus, paino, ika, sukupuoli, kaula, vyotaro, lantio, paiva):
        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (field)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        self.kaula = kaula
        self.vyotaro = vyotaro
        self.lantio = lantio
        self.bmi = fitness.laske_bmi(self.paino, self.pituus)
        self.fi_rasva = self.rasvaprosentti()
        if self.sukupuoli == 1:
            self.usa_rasva = self.usa_rasvaprosentti_mies(self.pituus, self.vyotaro, self.kaula)
        else:
            self.usa_rasva = self.usa_rasvaprosentti_nainen(self.pituus, self.vyotaro, self.lantio, self.kaula)
        self.punnitus_paiva = paiva
# Metodi painoindeksin laskemiseen
   

 # Metodi aikuisen rasvaprosentin laskemiseen
    def rasvaprosentti(self):
        if self.ika >= 18:
            self.rasvaprosentti = fitness.aikuisen_rasvaprosentti(self.bmi, self.ika, self.sukupuoli)
            return self.rasvaprosentti
        else:
            self.rasvaprosentti = fitness.lapsen_rasvaprosentti(self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti


    def usa_rasvaprosentti_mies(self, pituus, vyotaron_ymparys, kaulan_ymparys):
        """Laskee miehen rasvaprosentin USAn armeijan kaavoilla

        Args:
            pituus (float): pituus (cm)
            vyotaron_ymparys (float): vyötärön ympärysmitta (cm)
            kaulan_ymparys (float): kaulan ympärys cm

        Returns:
            float: rasvaprosentti
        """
        usa_rasvaprosentti =  fitness.usarasvaprosentti_mies(pituus,vyotaron_ymparys, kaulan_ymparys)
        return usa_rasvaprosentti
    
    def usa_rasvaprosentti_nainen(self, pituus, vyötaron_ymparys, lantion_ymparys, kaulan_ymparys):
        """Laskee naisen rasvaprosentin USAn armeijan kaavoilla

        Args:
            pituus (float): pituus (cm)
            vyotaron_ympärys (float): vyötärön ympärysmitta cm
            lantion_ymparys (float): lantion ympärysmitta cm
            kaulan_ymparys (float): kaulan ympärysmitta cm

        Returns:
            float: rasvaprosennti
        """
        usa_rasvaprosentti = fitness.usarasvaprosentti_nainen(pituus, vyötaron_ymparys, lantion_ymparys, kaulan_ymparys)
        return usa_rasvaprosentti


# JunioriKuntoilija on Kuntoilia luokan aliluokka
class JunioriKuntoilija(Kuntoilija):
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):
        super().__init__(nimi, pituus, paino, ika, sukupuoli)

    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.lapsen_rasvaprosentti(self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti

if __name__ == "__main__":

    kuntoilija = Kuntoilija('Mika', 171, 75, 60, 1, 30, 90, 0, '2023-04-21')
    print('bmi on', kuntoilija.bmi)
    print('suomalainen rasvaprosentti on:', kuntoilija.fi_rasva)
    print('amerikkalainen rasvaprosentti on:', kuntoilija.usa_rasva)
    
    '''kuntoilija = Kuntoilija('Kalle Kuntoilija', 171, 56, 18, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg')
    print(kuntoilija.nimi, 'painoindeksi on', kuntoilija.bmi)
    print(kuntoilija.nimi, 'rasvaprosentti on', kuntoilija.rasvaprosentti())

    juniorikuntoilija = JunioriKuntoilija('Aki', 171, 56, 17, 1)
    print(juniorikuntoilija.nimi,'rasvaprosentti on', juniorikuntoilija.rasvaprosentti())'''