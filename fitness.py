# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN    

# Kirjastot ja moduulit
import math

# Määritellään funktio painoindeksin laskentaan
def laske_bmi(paino, pituus):
    """Laskee painoindeksin (BMI)

    Args:
        paino (float): paino (kg)
        pituus (float): pituus (cm)

    Returns:
        float: painoindeksin kahden desimaalin tarkkuudella
    """
    pituus = pituus / 100 # muutetaan pituus metreiksi
    bmi = round(paino / pituus**2, 2)
    #print('Painoindeksisi on', bmi)
    return bmi

#Aikuisen rasvaprosentti = (1.20 × painoindeksi) + (0.23 × ikä) − (10.8 × sukupuoli) − 5.4

#jossa sukupuoli 1, jos mies ja 0, jos nainen. 

def aikuisen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee aikuisen kehon rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1 -> mies, 0 -> nainen

    Returns:
        float: Aikuisen kehon rasvaprosentti
    """

    rasvaprosentti = round(bmi * 1.20 + 0.23 * ika - 10.8 * sukupuoli - 5.4, 1)
    return rasvaprosentti

#Lapsen rasvaprosentti = (1.51 × painoindeksi) − (0.70 × ikä) − (3.6 × sukupuoli) + 1.4

def lapsen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee lapsen kehon rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1 -> poika, 0 -> tyttö

    Returns:
        float: Lapsen kehon rasvaprosentin
    """
    rasvaprosentti = round(bmi * 1.51 - 0.7 * ika - 3.6 * sukupuoli + 1.4, 1) 
    return rasvaprosentti


def usarasvaprosentti_mies(pituus, vyotaron_ymparys, kaulan_ymparys):
    """Laskee miehen rasvaprosentin USA:n armejan kaavalla

    Args:
        pituus (float): pituus (cm)
        vyötärön_ymp (float): vyötärön ympärysmitta (cm)
        kaulan_ymp (float): kaulan ympärysmitta (cm)


    Returns:
        float: rasvaprosentti
    """
    # Muutetaan mitat tuumiksi
    tuuma_pituus = pituus / 2.54
    tuuma_vyotaron_ymparys = vyotaron_ymparys / 2.54
    tuuma_kaulan_ymparys = kaulan_ymparys / 2.54
    # Lasketaan rasvaprosentti
    usarprosentti = round(86.01 * math.log10(tuuma_vyotaron_ymparys - tuuma_kaulan_ymparys) - 70.041 * math.log10(tuuma_pituus) + 36.76, 2)
    return usarprosentti 

def usarasvaprosentti_nainen(pituus, vyotaron_ymparys, lantion_ymparys, kaulan_ymparys):
    """Laskee naisen rasvaprosentin USA:n armejan kaavalla

    Args:
        pituus (float): pituus (cm)
        vyotaron_ymparys (float): vyötärön ympärysmitta (cm)
        kaulan_ymparys (float): kaulan ymparysmitta (cm)
    """
    tuuma_pituus = pituus / 2.54
    tuuma_vyotaron_ymparys = vyotaron_ymparys / 2.54
    tuuma_lantion_ymparys = lantion_ymparys / 2.54
    tuuma_kaulan_ymparys = kaulan_ymparys / 2.54
    
    usarprosentti = round(163.205 * math.log10(tuuma_vyotaron_ymparys + tuuma_lantion_ymparys - tuuma_kaulan_ymparys) - 97.684 * math.log10(tuuma_pituus) - 78.387, 2)
    return usarprosentti

if __name__ == '__main__':
    # Suoritetaan seuraavat rivit vain, jos tämä tiedosto on pääohjelma
    # Mahdollistaa funktioiden jakaamisen toisiin ohjelmiin
    # Muuttujat
    # Kysytään käyttäjältä tiedot
    pituus_teksti = input('Kuinka pitkä olet(cm)?')
    paino_teksti = input('Kuinka paljon painat(kg)?')
    ika_teksti = input('Kuinka vanha olet?')
    sukupuoli_teksti = input('Sukupuoli: mies - vastaa: 1 / nainen - vastaa: 0:') 
    vyotaron_ymparys_teksti = input('Mikä on vyötärön ympäryksesi? (cm):')
    kaulan_ymparys_teksti = input('Mikä on kaulan ympärysmitta? (cm):')
    lantion_ymparys_teksti = 0

    if sukupuoli_teksti == '0':
        lantion_ymparys_teksti = input('Mikä on lantion_ymparys? (cm):')

    pituus = float(pituus_teksti)
    paino = float(paino_teksti)
    ika = float(ika_teksti)
    sukupuoli = float(sukupuoli_teksti)
    oma_bmi = laske_bmi(paino, pituus)
    vyotaron_ymparys = float(vyotaron_ymparys_teksti)
    kaulan_ymparys = float(kaulan_ymparys_teksti)
    lantion_ymparys = float(lantion_ymparys_teksti)

    if ika >= 18:
        oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, sukupuoli)
    else:
        oma_rasvaprosentti = lapsen_rasvaprosentti(oma_bmi, ika, sukupuoli)

    print('Painoindeksisi on:', oma_bmi, 'ja kehon rasvaprosentti on:', oma_rasvaprosentti)
# Jos mies laske miehen kaavalla, muusa tapauksessa naisen kaavalla:
    if sukupuoli_teksti == '1':
        usa_rasvaprosentti = usarasvaprosentti_mies(pituus, vyotaron_ymparys, kaulan_ymparys)
        print('USA:n armeijan kaavalla rasvaprosentti on', usa_rasvaprosentti)
    else: 
        usa_rasvaprosentti = usarasvaprosentti_nainen(pituus, vyotaron_ymparys, lantion_ymparys, kaulan_ymparys)
        print('USA:n armeijan kaavalla rasvaprosentti on', usa_rasvaprosentti)
