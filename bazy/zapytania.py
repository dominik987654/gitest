#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Zapytania.py
#
import sqlite3

def kw_c(cur):
    cur.execute("""
        SELECT siedziba, SUM(placa) AS pensja
        FROM pracownicy, dzial
        WHERE pracownicy.id_dzial=dzial.id
        GROUP BY siedziba
        ORDER BY pensja ASC
    """)
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))
    
    def kw_d()
    cur.execute("""
        SELECT siedziba, SUM(placa) AS pensja
        FROM pracownicy, dzial
        WHERE pracownicy.id_dzial=dzial.id
        GROUP BY siedziba
        ORDER BY pensja ASC
    """)
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))
    

def main(args):
    con = sqlite3.connect('pracownicy.sqlite3')
    cur = con.cursor() #utworzenie kursora
    con.row_factory = sqlite3.Row
    
    kw_c(cur)
   
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
