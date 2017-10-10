#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#baza
#


import sqlite3
from dane import *     #importuj wszystko


def main(args):
    con = sqlite3.connect('pracownicy.sklite3')
    cur = con.cursor() #utworzenie kursora
    
    #utworzenie tabel w bazie danych    
    
    with open('pracownicy_z1geany.sql', 'r') as plik:
        skrypt = plik.read()
        cur.executescript(skrypt)
    
    premia = dane_z_pliku('premia.txt')
    premia = wyczysc_dane(premia,1)
    
    pracownicy = dane_z_pliku('pracownicy.txt')
    pracownicy = wyczysc_dane(pracownicy,5)
    
    dział = dane_z_pliku('dział.txt')
    
    print (pracownicy[0])
    
    cur.executemany('INSERT INTO premia VALUES(?,?)', premia )
    cur.executemany('INSERT INTO dzial VALUES(?,?,?)', dział )
    cur.executemany('INSERT INTO pracownicy(id, nazwisko, imie, stanowisko, data_zatr, placa, id_dzial) VALUES(?,?,?,?,?,?,?)', pracownicy )
    
    con.commit() #zatwardzenie operacji
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))