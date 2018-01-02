/*
 * struktury.cpp
 * 
 */

#include <iostream>
#include <iomanip>


using namespace std;



struct samochod {
    char marka[20];
    char model[20];
    int rokprodukcji;
    
    };
    
void wyswietlDane(samochod o){
    cout << setw(20) << "Marka : "  << o.marka << endl;
    cout << setw(20) << "Model : " << o.model << endl;
    cout << setw(4) << "Rok produkcji : " << o.rokprodukcji << endl;
};

void getSamochody(samochod t[], int ile){
    for(int i=0; i<=ile; i++){
        cout << "Podaj marke samochodu : ";
        cin >> t[i].marka;
        cout << "Podaj model samochodu : ";
        cin >> t[i].model;
        cout << "Podaj rok produkcji samochodu : ";
        cin >> t[i].rokprodukcji;
}
}
    
void drukujSamochody(samochod t[], int ile){
    for(int i=0; i<=ile; i++){
        cout << "Marka samochodu : ";
        cout << t[i].marka;
        cout << "Model samochodu : ";
        cout << t[i].model;
        cout << "Rok produkcji samochodu : ";
        cout << t[i].rokprodukcji;
}
}
int main(int argc, char **argv)
{
	//~samochod car1;
    //~cout << "Podaj marke samochodu : ";
    //~cin >> car1.marka;
    //~cout << "Podaj model samochodu : ";
    //~cin >> car1.model;
    //~cout << "Podaj rok produkcji samochodu : ";
    //~cin >> car1.rokprodukcji;
    //~wyswietlDane(car1);
    
    int ile;
    cout << "Ile samochodow?", cin >> ile;
    samochod tb[ile];
    getSamochody(tb, ile);
    drukujSamochody(tb, ile);
    
    
	return 0;
}

