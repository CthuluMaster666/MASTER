import sqlite3
from pathlib import Path

# Ścieżka do bazy danych
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "postacie.db"

def polacz():
    return sqlite3.connect(DB_PATH)

def utworz_tabele():
    conn = polacz()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS postacie (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            imie TEXT NOT NULL UNIQUE,
            sila INTEGER,
            zrecznosc INTEGER,
            inteligencja INTEGER,
            charyzma INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def zapisz_postac(imie, sila, zrecznosc, inteligencja, charyzma):
    conn = polacz()
    c = conn.cursor()
    try:
        c.execute('''
            INSERT INTO postacie (imie, sila, zrecznosc, inteligencja, charyzma)
            VALUES (?, ?, ?, ?, ?)
         ''', (imie, sila, zrecznosc, inteligencja, charyzma))
        conn.commit()
        print(f"Postać '{imie}' została zapisana.")
    except sqlite3.IntegrityError:
        print(f"Postać o imieniu '{imie}' już istnieje!")
    finally:
        conn.close()

def pobierz_postacie():
    conn = polacz()
    c = conn.cursor()
    c.execute("SELECT imie, sila, zrecznosc, inteligencja, charyzma FROM postacie")
    wyniki = c.fetchall()
    conn.close()
    return wyniki

def usun_postac(imie):
    conn = polacz()
    c = conn.cursor()
    c.execute("DELETE FROM postacie WHERE imie = ?", (imie,))
    conn.commit()
    conn.close()

# Utwórz tabelę automatycznie
utworz_tabele()