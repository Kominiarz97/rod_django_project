# Generated by Django 3.1 on 2020-10-27 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drony',
            fields=[
                ('id_drona', models.AutoField(primary_key=True, serialize=False)),
                ('nazwa', models.CharField(db_column='Nazwa', max_length=30)),
                ('pojemnosc_akumulatora', models.IntegerField(db_column='Pojemnosc_akumulatora')),
                ('predkosc_przelotowa', models.IntegerField(db_column='Predkosc_przelotowa')),
                ('oswietlenie', models.BooleanField(db_column='Oswietlenie')),
            ],
            options={
                'db_table': 'Drony',
            },
        ),
        migrations.CreateModel(
            name='PodzialTrasy',
            fields=[
                ('id_odcnika', models.AutoField(primary_key=True, serialize=False)),
                ('poczatek_odcinka', models.CharField(db_column='Poczatek_odcinka', max_length=30)),
                ('koniec_odcinka', models.CharField(db_column='Koniec_odcinka', max_length=30)),
                ('poziom_zagrozenia', models.IntegerField(db_column='Poziom_zagrozenia')),
            ],
            options={
                'db_table': 'Podzial_trasy',
            },
        ),
        migrations.CreateModel(
            name='Trasy',
            fields=[
                ('id_trasy', models.AutoField(primary_key=True, serialize=False)),
                ('stacja_poczatek', models.CharField(db_column='Stacja_poczatek', max_length=30)),
                ('stacja_koniec', models.CharField(db_column='Stacja_koniec', max_length=30)),
                ('dlugosc_trasy', models.IntegerField(db_column='Dlugosc_trasy')),
                ('nazwa_trasy', models.CharField(db_column='Nazwa_trasy', max_length=30)),
            ],
            options={
                'db_table': 'Trasy',
            },
        ),
        migrations.CreateModel(
            name='TypyOtoczenia',
            fields=[
                ('id_otoczenia', models.AutoField(primary_key=True, serialize=False)),
                ('typ', models.CharField(db_column='Typ', max_length=30)),
            ],
            options={
                'db_table': 'Typy_otoczenia',
            },
        ),
        migrations.CreateModel(
            name='Zagrozenia',
            fields=[
                ('id_zagrozenia', models.AutoField(primary_key=True, serialize=False)),
                ('typ', models.CharField(blank=True, db_column='Typ', max_length=30, null=True)),
            ],
            options={
                'db_table': 'Zagrozenia',
            },
        ),
        migrations.CreateModel(
            name='Zgloszenia',
            fields=[
                ('id_zgloszenia', models.AutoField(primary_key=True, serialize=False)),
                ('zdjecie', models.ImageField(db_column='Zdjecie', default=None, upload_to='')),
                ('data_zgloszenia', models.DateTimeField(db_column='Data_zgloszenia')),
                ('godz_zgloszenia', models.DateTimeField(db_column='Godz_zgloszenia')),
                ('lokalizacja_gps', models.CharField(db_column='Lokalizacja_gps', max_length=30)),
                ('zarejestrowane', models.BooleanField(db_column='Zarejestrowane', default=False)),
                ('zgloszenie_sluzbom', models.BooleanField(db_column='Zgloszenie_sluzbom', default=False)),
                ('id_drona', models.ForeignKey(db_column='id_drona', on_delete=django.db.models.deletion.DO_NOTHING, to='rod.drony')),
                ('id_odcinka_trasy', models.ForeignKey(db_column='id_odcinka_trasy', on_delete=django.db.models.deletion.DO_NOTHING, to='rod.podzialtrasy')),
                ('id_trasy', models.ForeignKey(db_column='id_trasy', on_delete=django.db.models.deletion.DO_NOTHING, to='rod.trasy')),
                ('id_uzytkownika', models.ForeignKey(blank=True, db_column='id_uzytkownika', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rodzaj_zagrozenia', models.ForeignKey(db_column='Rodzaj_zagrozenia', on_delete=django.db.models.deletion.DO_NOTHING, to='rod.zagrozenia')),
            ],
            options={
                'db_table': 'Zgloszenia',
            },
        ),
        migrations.AddField(
            model_name='podzialtrasy',
            name='trasa',
            field=models.ForeignKey(db_column='Trasa', on_delete=django.db.models.deletion.DO_NOTHING, to='rod.trasy'),
        ),
        migrations.AddField(
            model_name='podzialtrasy',
            name='typ_otoczenia',
            field=models.ForeignKey(db_column='Typ_otoczenia', on_delete=django.db.models.deletion.DO_NOTHING, to='rod.typyotoczenia'),
        ),
    ]
