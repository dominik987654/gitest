#ifndef LISTA_HPP
#define LISTA_HPP

struct Wezel{
    int wartosc;
    Wezel *wskaznik
};

class Drzewo{


private:

     *korzen;		


public:
    
    Drzewo();


    
    Wezel* stworzWezel(int);
    void dodajWezel(Wezel*, int);
    void wyswietlRosnaco(Wezel*);
    
    
};

#endif
