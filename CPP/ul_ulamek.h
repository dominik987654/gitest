#ifndef ULAMEK_H
#define ULAMEK_H

/*
* plik naglowkowy klasy ulamek
 */


class Ulamek{
private:
    int licznik;   //deklaracja skladowej wlasciwosci
    int mianownik;
public:
    Ulamek(int, int); //deklaracja konstruktora     
    void zapisz(int, int);  //deklaracja metody nie trzeba podawac zmiennych
    void wypisz();
    int get_l();
    int get_m();
    void skracaj();  //drukuje skrocona postac ulamka
};

#endif
