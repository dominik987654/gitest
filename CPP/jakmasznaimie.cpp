/*
 * jakmasznaimie.cpp
 * 
 * 
 */


#include <iostream>
using namespace std;   

int parzyste(int a){
    int i;
    for (i=0; i<=a; i+=2)
        cout << i << " " ;
    return i/2;
        
}
    
        
    
  

int main(int argc, char **argv)
{
    string imie;
    int wiek;
    int p;
    int a;
    
    cout << "Heloł" << endl;
    cout << "Podaj swoje imię" << endl;
    getline(cin,imie);
    cout << "Heloł " << imie << endl;
    cout << "Ile masz lat?" << endl;
    cin >> wiek;
    cout << "Urodziles sie w " << 2017-wiek <<  " roku.";
    p=26;
    if(wiek<p){
        cout << "Jestem starszy!" << endl;
        }else if(wiek==p){
            cout << "Mamy tyle samo lat!" << endl;
            }else
        cout << "Jestem mlodszy!" << endl;
    
    cout << "Podaj liczbe" << endl;
    cin >> a;
    cout << "Parzystych liczb jest : " << parzyste(a) << endl;
    
    
    //for(int i=0;i<=100;i+=2){
     //   cout << i << endl;
        
        
        
        

    return 0;
}

