#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj(tekst, klucz):
    i = 0
    for znak in tekst:
        wartosci = ord(znak.upper() - 64)
        wartosci2 = ord(klucz[i].upper() - 63)
        i +=1
        print wartosci, wartosci2


def main(args):
    tekst = raw_input("Podaj tekst : ")
    klucz = raw_input("Podaj klucz : ")
    print szyfruj(tekst, klucz)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
