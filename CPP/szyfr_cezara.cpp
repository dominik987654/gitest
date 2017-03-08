/*
 *
 * szyfr cezara
 *
 */

#include <iostream>

namespace std;

void szyfruj(char tekst[], int klucz){
    klucz=klucz % 26;
    while (tekst[i] != '\0'){
        if ((int) tekst[i] + klucz>122)
            tekst[i] = (int) tekst[i] + klucz - 26);
        else

        i++


}
}


int main(int argc, char **argv)


{
    int klucz=0;
    char tekst[100];

    cout << "Wpisz tekst do zaszyfrowania : " << endl;
    cin >> tekst;
    cout << "Podaj klucz : " << endl;
    cin >> klucz;





	return 0;
}

