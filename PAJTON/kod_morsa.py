#!/usr/bin/env python
# -*- coding: utf-8 -*-


def koduj(napis):
    litery = {'a':'*-','b':'-***','c':'-*-*'}
    for litera in napis:
        if litera !=' ':
            print litery[litera]

def main(args):
    #pobierz_napis
    koduj("abc")
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
