#ifndef DRZEWO_HPP
#define DRZEWO_HPP

#include <iostream>

struct Wezel{
    int wartosc;
    Wezel *lewy;
    Wezel *prawy;
};

class Drzewo{
    private:
        *korzen = NULL;
    
public:

        Drzewo();
        void DodajWezel(int, int);
        
};

#endif
