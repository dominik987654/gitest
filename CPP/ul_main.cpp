/*
 */


#include <iostream>


using namespace std;

class Ulamek{
private:
    int licznik;   //deklaracja skladowej wlasciwosci
    int mianownik;
public:
    Ulamek(int, int); //deklaracja konstruktora
     
    void zapisz(int, int);  //deklaracja metody nie trzeba podawac zmiennych
    void wypisz(){
        cout << licznik << "/" << mianownik;
    }
    int get_l(){
        return licznik;
    }
    int get_m(){
        return mianownik;
    }
void skracaj();  //drukuje skrocona postac ulamka


};

void Ulamek::skracaj(){
    ; //algorytm euklidesa

void Ulamek::zapisz(int l, int m){
    licznik = l;
    if(m!=0) mianownik = m;
    else {
        cout << "Nie dziel przez zero!";
        exit(1);        
    }
}

Ulamek::Ulamek(int l, int m){
    licznik = l;
    if(m!=0) mianownik = m;
    else {
        cout << "Nie dziel przez zero!";
        exit(1);        
    }
}


int main(int argc, char **argv)
{
	//Ulamek u1, u2; //deklaracja obiektu
    Ulamek u1(3,7); //definicja obiektu
    Ulamek u2(1,4); //definicja obiektu
    //u1.zapisz(3,7);
    //u2.zapisz(1,4);
    cout << "Ulamek 1 : " << endl;
    u1.wypisz();
    cout << "Ulamek 2 : " << endl;
    u2.wypisz();
    
    u1.zapisz(7,9);
    cout << "Licznik : " << u1.get_l() << endl;
    cout << "Mianownik : " << u1.get_m() << endl;
    
    Ulamek u3(u1.get_l(), u1.get_m());
    u3.wypisz();
    
    
	return 0;
}

