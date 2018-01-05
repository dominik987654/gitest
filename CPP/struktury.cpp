/*
 * struktury.cpp
 * 
 */

#include <iostream>
#include <iomanip>
#include <fstream>



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
    
void zapiszDane(samochod t[], int ile){
    ofstream plik("samochody.txt", ios::app);
    if (!plik.is_open()) {
        cout << "Błąd otwarcia pliku!";
    } else  {
        for(int i=0; i<ile; i++){
            cout << t[i].marka << " ," << t[i].model << " ," << t[i].rokprodukcji << endl;
            plik << t[i].marka << " ," << t[i].model << " ," << t[i].rokprodukcji << endl;
        }
    }
}


void drukujSamochody(samochod t[], int ile){
    for(int i=0; i<=ile; i++){
        cout << "Marka samochodu : ";
        cout << t[i].marka << " ";
        cout << "Model samochodu : ";
        cout << t[i].model << " ";
        cout << "Rok produkcji samochodu : ";
        cout << t[i].rokprodukcji << " ";
        cout << endl;
}
}

int czytajDane(samochod t[] ){
    ifstream plik("samochody.txt"):
    string linia;
    int i=0;
    if (plik.is_open()) {
        while(getline(plik, linia)){
            cout << linia << endl;
            i++;
        }
    } else { 
        cout << "Błąd otwarcia pliku!";
    }
    return i;
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
    //getSamochody(tb, ile);
    //drukujSamochody(tb, ile);
    //zapiszDane(tb, ile);
    cout << czytajDane(tb) << endl;
	return 0;
}

