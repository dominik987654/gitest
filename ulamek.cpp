/*
 * ulamek.cpp
 * 
 * Copyright 2018  <>
 * 
 */

#include <iostream>
#include "ul_ulamek.h"

using namespace std;

Ulamek::Ulamek(int l, int m){
    licznik = l;
    if (m != 0) mianownik = m;
    else{
        cout << "Mianownik nie moze byc zerem!";
        exit(1);
        }
    }

void Ulamek::zapisz(int l, int m){
    licznik = l;
    if (m != 0) mianownik = m;
    else{
        cout << "Mianownik nie moze byc zerem!";
        exit(1);
        }
    }
 
void Ulamek::wypisz(){
        cout << licznik << "/" << mianownik << endl;
        }
        
void Ulamek::skracaj(int l, int m){
    int a = l;
    int b = m;
    
    do{
    	if(a > b) a = a - b; 
    		else b = b - a;
	} 
	while (a != b);
	
	cout << "Ulamek po skroceniu: " << l/a << "/" << m/a << endl;


	 //wykorzystaj algorytm euklidesa optymalny
    }

int Ulamek::get_l(){
        return licznik;
        }

        
int Ulamek::get_m(){
        return mianownik;
}
