# -*- coding: utf-8 -*-

from peewee import *


baza_plik = "szkola.db"
if os.path.exists(baza_plik):
    os.remove(baza_plik)
baza = SqliteDatabase(baza_plik)  # ':memory:'


class BazaModel(Model):
    class Meta:
        database = baza


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = IntegerField(null=False)
    klasa_id = ForeignKeyField(Klasy, related_name = 'Ocen')
    egzhum = DecimalField(decimal_places = 2, default = 0, null=False)
    egzmat = DecimalField(decimal_places = 2, default = 0, null=False)
    egzjez = DecimalField(decimal_places = 2, default = 0, null=False)



class Klasa(BazaModel):
    nazwa = CharField(null=False)
    rok_naboru = IntegerField(null=False)
    rok_matury = IntegerField(null=False)


class Przedmiot(BazaModel):
    nazwa = CharField(null=False)
    imien = CharField(null=False)
    nazwiskon = CharField(null=False)
    plecn = IntegerField(null=False)


class Ocena(BazaModel):
    datad = DataField(null=False)
    uczen_id = ForeignKeyField(Uczniowie, related_name = 'Ocena')
    przedmiot_id = ForeignKeyField(Przedmioty, related_name = 'id')
    ocena = DecimalField(null=False)


baza.connect()  # nawiązujemy połączenie z bazą
baza.create_tables([Uczen, Klasa, Przedmiot, Ocena], True)  # tworzymy tabele
