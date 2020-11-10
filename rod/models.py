from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Drony(models.Model):
   id_drona = models.AutoField(primary_key=True)
   nazwa = models.CharField(db_column='Nazwa', max_length=30)
   pojemnosc_akumulatora = models.IntegerField(db_column='Pojemnosc_akumulatora')
   predkosc_przelotowa = models.IntegerField(db_column='Predkosc_przelotowa')
   oswietlenie = models.BooleanField(db_column='Oswietlenie')
   class Meta:
       db_table = 'Drony'


class PodzialTrasy(models.Model):
   id_odcnika = models.AutoField(primary_key=True)
   poczatek_odcinka = models.CharField(db_column='Poczatek_odcinka', max_length=30)
   koniec_odcinka = models.CharField(db_column='Koniec_odcinka', max_length=30)
   typ_otoczenia = models.ForeignKey('TypyOtoczenia', models.DO_NOTHING, db_column='Typ_otoczenia')
   poziom_zagrozenia = models.IntegerField(db_column='Poziom_zagrozenia')
   trasa = models.ForeignKey('Trasy', models.DO_NOTHING, db_column='Trasa')

   class Meta:
       db_table = 'Podzial_trasy'




class Trasy(models.Model):
   id_trasy = models.AutoField(primary_key=True)
   stacja_poczatek = models.CharField(db_column='Stacja_poczatek', max_length=30)
   stacja_koniec = models.CharField(db_column='Stacja_koniec', max_length=30)
   dlugosc_trasy = models.IntegerField(db_column='Dlugosc_trasy')
   nazwa_trasy = models.CharField(db_column='Nazwa_trasy', max_length=30)

   class Meta:
       db_table = 'Trasy'


class TypyOtoczenia(models.Model):
   id_otoczenia = models.AutoField(primary_key=True)
   typ = models.CharField(db_column='Typ', max_length=30)

   class Meta:
       db_table = 'Typy_otoczenia'


class Zagrozenia(models.Model):
   id_zagrozenia = models.AutoField(primary_key=True)
   typ = models.CharField(db_column='Typ', max_length=30, blank=True, null=True)  # Field name made lowercase.

   class Meta:
       db_table = 'Zagrozenia'



class Zgloszenia(models.Model):
   id_zgloszenia = models.AutoField(primary_key=True)
   zdjecie = models.BinaryField(db_column="Zdjecie",blank=True)
   data_zgloszenia = models.DateField(db_column='Data_zgloszenia', blank=True, null=True)
   godz_zgloszenia = models.TimeField(db_column='Godz_zgloszenia', blank=True, null=True)
   id_drona = models.ForeignKey(Drony, models.DO_NOTHING, db_column='id_drona', blank=True, null=True)
   id_trasy = models.ForeignKey(Trasy, models.DO_NOTHING, db_column='id_trasy', blank=True, null=True)
   id_odcinka_trasy = models.ForeignKey(PodzialTrasy, models.DO_NOTHING, db_column='id_odcinka_trasy', blank=True, null=True)
   rodzaj_zagrozenia = models.ForeignKey(Zagrozenia, models.DO_NOTHING, db_column='Rodzaj_zagrozenia', blank=True, null=True)
   lokalizacja_gps = models.CharField(db_column='Lokalizacja_gps', max_length=30, blank=True)
   zarejestrowane = models.BooleanField(db_column='Zarejestrowane', default=False, blank=True)
   id_uzytkownika = models.ForeignKey(User, models.CASCADE, db_column='id_uzytkownika', blank=True, null=True)
   zgloszenie_sluzbom = models.BooleanField(db_column='Zgloszenie_sluzbom', default=False, blank=True)

   class Meta:
      db_table = 'Zgloszenia'


