# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Kpd(models.Model):
    kod = models.AutoField(db_column='Код', primary_key=True)  # Field name made lowercase.
    platform = models.ForeignKey('', models.DO_NOTHING, db_column='№АЗС', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    throughput = models.CharField(db_column='Скорость передачи данных, Кбит/с', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_mile = models.CharField(db_column='Технология последней мили', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service = models.CharField(db_column='Услуга', max_length=255, blank=True, null=True)  # Field name made lowercase.
    provider = models.CharField(max_length=255, blank=True, null=True)
    tarif = models.FloatField(db_column='Сумма в месяц', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contract_number_legal = models.CharField(db_column='Номер и дата Договора (Юрид)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    contract_number_system = models.CharField(db_column='Номер договора системн', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contract_date = models.DateTimeField(db_column='Дата заключениея договора', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    b_z = models.IntegerField(db_column='№Б-З', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    date_b_z = models.DateTimeField(db_column='Дата заключения Б-З', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contract_ends = models.DateTimeField(db_column='Договор дейтсвует до', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note = models.CharField(db_column='Примечание', max_length=511, blank=True, null=True)  # Field name made lowercase.
    number_in_docs_from_prov = models.IntegerField(db_column='Номер в документах providerа', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tku = models.NullBooleanField(db_column='Наличие ТКУ')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    account = models.CharField(db_column='Лицевой счет', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Common_KPD'


class Fpsu(models.Model):
    kod = models.AutoField(db_column='Код', primary_key=True)  # Field name made lowercase.
    invent_number = models.CharField(db_column='Инвентарный №', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    serial_number = models.CharField(db_column='Серийный №', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_OS = models.CharField(db_column='Название основного средства', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    system_name = models.CharField(db_column='Системное имя', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    platform = models.CharField(db_column='Местонахождение', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='Состояние', max_length=255, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Примечание', max_length=511, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FPSU'


class Rezerve(models.Model):
    kod = models.AutoField(db_column='Код', primary_key=True)  # Field name made lowercase.
    invent_number = models.CharField(db_column='Инвентарный №', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    serial_number = models.CharField(db_column='Серийный №', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_OS = models.CharField(db_column='Название основного средства', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    int_ext = models.CharField(db_column='Вид монтаж', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    install_date = models.DateTimeField(db_column='Дата монтажа', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    system_name = models.DateTimeField(db_column='Системное имя', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    platform = models.CharField(db_column='Местонахождение', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='Состояние', max_length=255, blank=True, null=True)  # Field name made lowercase.
    b_z = models.CharField(db_column='№ Б-З', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    note = models.CharField(db_column='Примечание', max_length=511, blank=True, null=True)  # Field name made lowercase.
    provider_reserve = models.CharField(db_column='Оператор', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iccid_common_provider = models.CharField(db_column='ICCID (основной оператор)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    msisdn_common_provider = models.CharField(db_column='MSISDN(основной оператор)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    imsi_common_provider = models.CharField(db_column='IMSI(основной оператор)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sim_state = models.CharField(db_column='Статус SIM-карты', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    iccid_reserve_provider = models.CharField(db_column='ICCID (оператор для смены)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    msisdn_reserve_provider = models.CharField(db_column='MSISDN(оператор для смены)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    imsi_reserve_provider = models.CharField(db_column='IMSI(оператор для смены)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'modems_rezerv'


class Switches(models.Model):
    kod = models.AutoField(db_column='Код', primary_key=True)  # Field name made lowercase.
    invent_number = models.CharField(db_column='Инвентарный №', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    serial_number = models.CharField(db_column='Серийный №', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_OS = models.CharField(db_column='Название основного средства', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    system_name = models.CharField(db_column='Системное имя', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    platform = models.CharField(db_column='Местонахождение', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='Состояние', max_length=255, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Примечание', max_length=511, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Коммутаторы'
# Unable to inspect table 'Маршрутизаторы'
# The error was: permission denied for relation Маршрутизаторы


class OS(models.Model):
    os_number = models.AutoField(db_column='№', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    platform = models.CharField(db_column='Объект', max_length=255, blank=True, null=True)  # Field name made lowercase.
    router = models.CharField(db_column='Маршрутизатор', max_length=255, blank=True, null=True)  # Field name made lowercase.
    switch = models.CharField(db_column='Коммутатор', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modem = models.CharField(db_column='Модем', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fpsu = models.CharField(db_column='ФПСУ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    server = models.CharField(db_column='Сервер', max_length=255, blank=True, null=True)  # Field name made lowercase.
    server_cabinet = models.CharField(db_column='Серверный шкаф', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mediagetway = models.CharField(db_column='Медиаконвертер', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ups = models.CharField(db_column='ИБП', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ОС'


class Platform(models.Model):
    platform = models.CharField(db_column='Наименование', primary_key=True, max_length=255)  # Field name made lowercase.
    address = models.CharField(db_column='Адрес', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Регион', max_length=255, blank=True, null=True)  # Field name made lowercase.
    oil_base = models.CharField(db_column='Нефтебаза', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Широта', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Долгота', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='Состояние', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Примечания', max_length=511, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Объект'


class Other(models.Model):
    kod = models.AutoField(db_column='Код', primary_key=True)  # Field name made lowercase.
    invent_number = models.CharField(db_column='Инвентарный №', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    serial_number = models.CharField(db_column='Серийный №', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_OS = models.CharField(db_column='Название основного средства', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    system_name = models.CharField(db_column='Системное имя', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    platform = models.CharField(db_column='Местонахождение', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='Состояние', max_length=255, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Примечание', max_length=511, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Прочее'


class Servers(models.Model):
    kod = models.AutoField(db_column='Код', primary_key=True)  # Field name made lowercase.
    invent_number = models.CharField(db_column='Инвентарный №', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    serial_number = models.CharField(db_column='Серийный №', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_OS = models.CharField(db_column='Название основного средства', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    system_name = models.CharField(db_column='Системное имя', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    platform = models.CharField(db_column='Местонахождение', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='Состояние', max_length=255, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Примечание', max_length=511, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Серверы'


class Phones(models.Model):
    kod = models.AutoField(db_column='Код', primary_key=True)  # Field name made lowercase.
    platform = models.CharField(db_column='Объект', blank=True, null=True)  # Field name made lowercase.
    phone_number = models.TextField(db_column='№ телефона', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    count = models.FloatField(db_column='Кол-во, шт', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    abon_number_tarif = models.FloatField(db_column='Действующий тариф, за  абон линию', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    local_unlim_tarif = models.FloatField(db_column='Тариф, за местный безлим', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    local_tarif = models.FloatField(db_column='цена мин. местн.(нет безлимта)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    voip_tarif = models.FloatField(db_column='Абон за VoIP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vpn_for_voip_tarif = models.FloatField(db_column='Абон за VoIP_(VPN-канал)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'Телефоны'
