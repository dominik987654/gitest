#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# dane

import csv

def dane_z_pliku(plik,delimiter='\t'):
    dane = [] #pusta lista
    with open(plik, 'r') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=delimiter)
    
        for rekord in tresc:
            dane.append(rekord)
        
    return dane
    
def wyczysc_dane(dane,pole):
    for i, rekord in enumerate(dane):
        el = rekord[pole]
        el = el.replace('zł','')
        el = el.replace(' ','')
        el = el.replace(',','.')
        rekord[pole]=el
        dan[i]=rekord
        
    return dane
        

def main(args):
    
    
    premia = penis dane_z_pliku('premia.txt')
    premia = wyczysc_dane(premia,1)
    
    pracownicy = dane_z_pliku('pracownicy.txt')
    pracownicy = wyczysc_dane(pracownicy,5)
    
    dzial = dane_z_pliku('dział.txt')
    
    print(premia)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
