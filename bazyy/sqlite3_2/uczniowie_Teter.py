#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#zapytania.py

import sqlite3

def wyniki(cur):
    wyniki = cur.fetchall() #pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))



def kw_a(cur):
    cur.execute('''
        SELECT Imie, Nazwisko, tbKlasy.klasa
        FROM tbUczniowie, tbKlasy
        WHERE tbUczniowie.klasaID=tbKlasy.IDklasy
        AND tbKlasy.Klasa = '1A'
        ''')
        
        
def kw_b(cur):
    cur.execute('''
        SELECT MAX(EgzHum)
        FROM tbUczniowie
        ''')
        
        
def kw_c(cur):
    cur.execute("""
        SELECT AVG(EgzMat)
        FROM tbUczniowie, tbKlasy
        WHERE tbUczniowie.klasaID=tbKlasy.IDklasy
        AND tbKlasy.Klasa = '1A'
        """)
        
        
def kw_d(cur):
    cur.execute("""
        SELECT Imie, Nazwisko, tbOceny.Ocena
        FROM tbUczniowie, tbOceny
        WHERE tbOceny.UczenID = tbUczniowie.IDucznia
        AND Imie = "Dorota" 
        AND Nazwisko = "Nowak"
        """)
        
        
def kw_e(cur):
    cur.execute("""
        SELECT AVG(Ocena)
        FROM tbOceny, tbPrzedmioty
        WHERE strftime('%m', datad) LIKE '10'
        AND tbOceny.PrzedmiotID = tbPrzedmioty.IDPrzedmiotu
        AND tbPrzedmioty.Przedmiot = 'fizyka'
       """)
       
def dodaj(cur): #dodawanie 
    cur.execute("""
        INSERT INTO tbKlasy
        VALUES (?,?,?,?)
    """,[None,'3C',2015,2018])
    
def aktualizuj(cur):
    cur.execute("""
        UPDATE tbKlasy
        SET klasa = ?
        WHERE IDKlasy = ?
    """,['3D',13])
    
def akt(cur):
    cur.execute("""
    UPDATE tbUczniowie
    SET EgzJez = ?
    WHERE Imie = ?
    AND Nazwisko = ?
    AND IDucznia = ?
    """, [35, 'Paulina', 'Dziedzic', 135])
    
    
def usun(cur):
    cur.execute('DELETE FROM tbKlasy WHERE klasa = ? AND roknaboru = ?', ['3B', 2015])
    
    
def main(args):
    con = sqlite3.connect('szkola.db')
    cur = con.cursor() #utworzenie kursora
    con.row_factory = sqlite3.Row
    
    #dodaj(cur)
    #aktualizuj(cur)
    #usun(cur)
    akt(cur)
    con.commit()
    wyniki(cur.execute('SELECT * FROM tbUczniowie'))
    #wyniki(cur.execute('SELECT * FROM tbKlasy'))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
