#!/usr/bin/env python
# -*- coding: utf-8 -*-
#




import csv

def dane_z_pliku(plik,delimiter='\t'):
    dane = [] #pusta lista
    with open(plik, 'r') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=delimiter)
    
        for rekord in tresc:
            dane.append(rekord)
    
    return dane

def wyczysc_dane(dane, pole):
    for i, rekord in enumerate(dane):
        el = rekord[pole]
        el = el.replace('zł','')
        el = el.replace(' ','')
        el = el.replace(',','.')
        rekord[pole] = el
        dane[i] = rekord
        
    return dane


def main(args):
    dane = dane_z_pliku('premia.txt')
    #dane_z_pliku('dział.txt')
    #dane_z_pliku('pracownicy.txt')
    premia = wyczysc_dane(dane,1)
    print(premia)
    #print (pracownicy)
    return 0









 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
