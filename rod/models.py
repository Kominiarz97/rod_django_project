# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PlatformyLatajace(models.Model):
    id_drona = models.AutoField(primary_key=True)
    nazwa = models.CharField(db_column='Nazwa', max_length=30)  # Field name made lowercase.
    pojemonosc_akumulatora = models.IntegerField(db_column='Pojemonosc_akumulatora')  # Field name made lowercase.
    predkosc_przelotowa = models.IntegerField(db_column='Predkosc_przelotowa', blank=True, null=True)  # Field name made lowercase.
    oswietlenie = models.BooleanField(db_column='Oswietlenie', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Platformy_latajace'


class PodzialTrasy(models.Model):
    id_odcnika = models.AutoField(primary_key=True)
    poczatek_odcinka = models.IntegerField(db_column='Poczatek_odcinka')  # Field name made lowercase.
    koniec_odcinka = models.IntegerField(db_column='Koniec_odcinka')  # Field name made lowercase.
    typ_otoczenia = models.ForeignKey('TypyOtoczenia', models.DO_NOTHING, db_column='Typ_otoczenia')  # Field name made lowercase.
    poziom_zagrozenia = models.IntegerField(db_column='Poziom_zagrozenia')  # Field name made lowercase.
    trasa = models.ForeignKey('Trasy', models.DO_NOTHING, db_column='Trasa')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Podzial_trasy'


class Trasy(models.Model):
    id_trasy = models.AutoField(primary_key=True)
    stacja_poczatek = models.CharField(db_column='Stacja_poczatek', max_length=30)  # Field name made lowercase.
    stacja_koniec = models.CharField(db_column='Stacja_koniec', max_length=30)  # Field name made lowercase.
    dlugosc_trasy = models.IntegerField(db_column='Dlugosc_trasy')  # Field name made lowercase.
    nazwa_trasy = models.CharField(db_column='Nazwa_trasy', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Trasy'


class TypyOtoczenia(models.Model):
    id_otoczenia = models.AutoField(primary_key=True)
    typ = models.CharField(db_column='Typ', max_length=-1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Typy_otoczenia'


class Uzytkownicy(models.Model):
    id_uzytkownika = models.AutoField(primary_key=True)
    imie = models.CharField(db_column='Imie', max_length=30)  # Field name made lowercase.
    nazwisko = models.CharField(db_column='Nazwisko', max_length=30)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30, blank=True, null=True)  # Field name made lowercase.
    numer_telefonu = models.IntegerField(db_column='Numer_telefonu', blank=True, null=True)  # Field name made lowercase.
    haslo = models.CharField(db_column='Haslo', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Uzytkownicy'


class Zagrozenia(models.Model):
    id_zagrozenia = models.AutoField(primary_key=True)
    typ = models.CharField(db_column='Typ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    skala_zagrozenia = models.SmallIntegerField(db_column='Skala_zagrozenia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zagrozenia'


class Zgloszenia(models.Model):
    id_zgloszenia = models.AutoField(primary_key=True)
    id_drona = models.ForeignKey(PlatformyLatajace, models.DO_NOTHING, db_column='id_drona')
    id_trasy = models.ForeignKey(Trasy, models.DO_NOTHING, db_column='id_trasy')
    id_odcinka_trasy = models.ForeignKey(PodzialTrasy, models.DO_NOTHING, db_column='id_odcinka_trasy')
    rodzaj_zagrozenia = models.ForeignKey(Zagrozenia, models.DO_NOTHING, db_column='Rodzaj_zagrozenia')  # Field name made lowercase.
    lokalizacja_gps_n = models.CharField(db_column='Lokalizacja_gps_N', max_length=30)  # Field name made lowercase.
    lokalizacja_gps_e = models.CharField(db_column='Lokalizacja_gps_E', max_length=30)  # Field name made lowercase.
    id_uzytkownika = models.ForeignKey(Uzytkownicy, models.DO_NOTHING, db_column='id_uzytkownika', blank=True, null=True)
    zgloszenie_sluzbon = models.BooleanField(db_column='Zgloszenie_sluzbon', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zgloszenia'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
