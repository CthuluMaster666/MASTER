from CthuluTheGame.Klasy.Postac import Postac
from CthuluTheGame.baza import polacz

def wczytaj_postac_z_bazy(imie):
    conn = polacz()
    c = conn.cursor()
    c.execute("SELECT imie, sila, zrecznosc, inteligencja, charyzma FROM postacie WHERE imie = ?", (imie,))
    rekord = c.fetchone()
    conn.close()

    if rekord:
        postac = Postac(rekord[0])
        postac.sila.wartosc = rekord[1]
        postac.zrecznosc.wartosc = rekord[2]
        postac.inteligencja.wartosc = rekord[3]
        postac.charyzma.wartosc = rekord[4]
        return postac
    else:
        print(f"Nie znaleziono postaci o imieniu: {imie}")
        return None