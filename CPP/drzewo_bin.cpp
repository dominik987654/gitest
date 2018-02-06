/*
 * drzewo_bin.cpp
*/

#include <iostream>

using namespace std;

struct Wezel {
    int wartosc;
    Wezel *lewy;
    Wezel *prawy;    
} *korzen= NULL; // definicja struktury i utworzenie wskaznika korzen


Wezel* stworzWezel(int wartosc){
    Wezel *nowyWezel = new Wezel;
    nowyWezel -> wartosc = wartosc;
    nowyWezel -> lewy = NULL;
    nowyWezel -> prawy = NULL;
    
    return nowyWezel;
}

void dodajWezel(Wezel *wezel, int wartosc){
    if (korzen = NULL) { // drzewo jest puste
        korzen = stworzWezel(wartosc); // utworzenie pierwszego elementu drzewa
        } else {
            if (wartosc < wezel -> wartosc){
                if(wezel -> lewy !=NULL) {
                    dodajWezel(wezel -> lewy, wartosc); // rekurencyjne wywolanie dodania do lewego poddrzewa
                }else{ // lewy potomek nie istnieje
                    wezel -> lewy = stworzWezel(wartosc); // nowy wezel
        } else { //wartosc wieksza
            if (wartosc > wezel -> wartosc){
                if(wezel -> prawy !=NULL) {
                    dodajWezel(wezel -> prawy, wartosc); // rekurencyjne wywolanie dodania do lewego poddrzewa
                }else{ // prawy potomek nie istnieje
                    wezel -> prawy = stworzWezel(wartosc); // nowy wezel
        ;
        }
    }
}
int main(int argc, char **argv)
{
	
	return 0;
}

