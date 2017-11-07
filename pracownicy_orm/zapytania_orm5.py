# -*- coding: utf-8 -*-


from peewee import *

baza_plik = 'pracownicy.sqlite3'
baza = SqliteDatabase(baza_plik)

class BazaModel(Model):
    class Meta:
        database = baza

class Premia(BazaModel):
    id = CharField(primary_key = True)
    premia = DecimalField()

class Dzial(BazaModel):
    id = IntegerField(primary_key = True)
    nazwa = CharField()
    siedziba = CharField()

class Pracownik(BazaModel):
    id = CharField(primary_key = True)
    nazwisko = CharField()
    imie = CharField()
    stanowisko = ForeignKeyField(Premia, related_name = 'pracownicy')
    data_zatr = CharField()
    placa = DecimalField(decimal_places = 2)
    id_dzial = ForeignKeyField(Dzial, related_name = 'pracownicy')
    premia = DecimalField(decimal_places = 2, default = 0)


baza.connect()


def kwerenda_c():
    query = (Dzial
        .select(Dzial.siedziba, fn.suma(Pracownik.placa).alias('place'))
        .join(Pracownik)
        .group_by(Dzial.siedziba)
        .order_by('place').asc()
        )

    for obj in query:
        print(obj.siedziba, obj.place)

def kwerenda_d():
    query = (Pracownik
        .select(Dzial.id, Dzial.nazwa,Pracownik.imie, Pracownik.nazwisko)
        .join(Dzial)
        .order_by(Dzial.nazwa).asc()
        )

    for obj in query:
        print(obj.id_dzial.id, obj.id_dzial.nazwa, obj.imie, obj.nazwisko)

def kwerenda_e():
    query = (Pracownik
        .select()
        .join(Premia)
        )

    for obj in query:
        print(obj.imie, obj.nazwisko, obj.stanowisko)

kwerenda_d()
