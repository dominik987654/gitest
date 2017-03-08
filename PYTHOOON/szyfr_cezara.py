#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj_cezar(tekst, klucz):
    klucz = int(klucz) % 26
    for znak in tekst:
        znak = znak.lower()
        if ord(znak) + klucz > 122:
            szyfrogram += chr(ord(znak) + klucz - 26)
        else:
            szyfrogram += chr(ord(znak) + klucz)
    return szyfrogram


def main(args):
    tekst = raw_input("Podaj tekst : ")
    klucz = raw_input("Podaj klucz : ")
    print szyfruj_cezar(tekst, klucz

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
