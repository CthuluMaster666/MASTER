from CthuluTheGame.Klasy.Postac import Postac
from CthuluTheGame.baza import zapisz_postac

def tworzeniepostaci(imiepostaci):
    gracz = Postac(imiepostaci)

    zapisz_postac(
        imie=gracz.imie,
        sila=gracz.sila.wartosc,
        zrecznosc=gracz.zrecznosc.wartosc,
        inteligencja=gracz.inteligencja.wartosc,
        charyzma=gracz.charyzma.wartosc
    )