#!/usr/bin/env python
# -*- coding: utf-8 -*-

def osoba(imie, nazwisko, wiek):
    return {'imie':imie, 'nazwisko':nazwisko, 'wiek':wiek,}

def pobierzDane(ile):
    lista = []
    for i in range(0,int(ile)):
        imie = input('Podaj imie :')
        nazwisko = input('Podaj nazwisko :')
        wiek = input('Podaj wiek :')
        lista.append(osoba(imie, nazwisko, wiek))



def main(args):
    #osoba1 = osoba('Zbyszek', 'Ciasny', '43'):
    #print (osoba1.keys())
    #print (osoba1.values())
    #print (osoba1['nazwisko'])
    ile = input('Ile osob wprowadzisz?')
    lista = pobierzDane(ile)
    print(lista)
    return 0



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
