#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jakmasznaimie.py 

def parzyste(n):
    ile=list(range(0,n+1,2))
    print(ile)
    return len(ile)

def main(args):
    return 0

if __name__ == '__main__':
    
    print("helo")
    
    imie=input("jak masz na imie?")
    print("hello ",imie,)
    wiek=int(input("ile masz lat?"))
    
    print("Urodziles sie w ", 2017-wiek)
    
    c=1991
    rok=2017-wiek
    
    if c==rok:
            print("mam tyle lat co Ty!")
    elif c<rok:
            print("Jestem od Ciebie starszy!")
    elif c>rok:
            print("Jestem młodszy od Ciebie!")
    n=int(input("podaj liczbe : "))
    print("parzystych : ", parzyste(n))
    
    
    import sys
    sys.exit(main(sys.argv))
