#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#zapytania.py

import sqlite3


def kw_c(cur):
    cur.execute('''
        SELECT siedziba, SUM(placa) AS pensja
        FROM pracownicy, dzial
        WHERE pracownicy.id_dzial=dzial.id
        GROUP BY siedziba
        ORDER BY pensja ASC
    ''')
    wyniki = cur.fetchall() #pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))


def kw_d(cur):
    nazwa = input("podaj nazwe dzialu : ")
    print(nazwa)
    siedz = input("podaj siedzibe : ")
    
    cur.execute('''
            SELECT siedziba, imie, dzial.id, dzial.nazwa
            FROM pracownicy, dzial
            WHERE pracownicy.id_dzial=dzial.id
            AND dzial.nazwa = ?
            AND siedziba = ?
        ''', (nazwa, siedz))
    wyniki = cur.fetchall() #pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))


def kw_e(cur):
    cur.execute("""
        SELECT nazwisko, stanowisko, pracownicy.placa *
        
        (SELECT premia.premia 
        FROM premia
        WHERE pracownicy.stanowisko = premia.id)
        AS premia
        FROM pracownicy
        ORDER BY premia DESC
        """)
    wyniki = cur.fetchall() #pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))


def kw_f(cur):
    kobiety = cur.execute("""
        SELECT AVG(placa)
        FROM pracownicy
        WHERE imie LIKE '%a'
        """)
    wyniki = kobiety.fetchall() #pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))
        
    men = cur.execute("""
        SELECT AVG(placa)
        FROM pracownicy
        WHERE imie NOT LIKE '%a'
        """)
        
    wyniki = men.fetchall() #pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))


def kw_g(cur):
    cur.execute("""
        SELECT imie, nazwisko,stanowisko (JulianDay())
        
       
       """)
    wyniki = cur.fetchall() #pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))
 
 
 

def main(args):
    con = sqlite3.connect('pracownicy.sqlite3')
    cur = con.cursor() #utworzenie kursora
    con.row_factory = sqlite3.Row
    
    kw_f(cur)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
