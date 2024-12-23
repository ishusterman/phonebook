from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin



class Otdel(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(verbose_name="Отделение", max_length=60, blank=False)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

class Building(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(verbose_name="Корпус", max_length=60, blank=False)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'

class Person(models.Model):
    id = models.AutoField(primary_key=True)

    Otdel = models.ForeignKey(Otdel, verbose_name="Отдел", blank=True, null=True)
    Building = models.ForeignKey(Building, verbose_name="Корпус", blank=True, null=True)
    Floor = models.CharField(verbose_name="Этаж", max_length=10, blank=True)
    Room = models.CharField(verbose_name="Кабинет", max_length=10, blank=True)

    SurName = models.CharField(verbose_name="Фамилия", max_length=20, blank=True)
    FirstName = models.CharField(verbose_name="Имя", max_length=20, blank=True)
    Patronymic = models.CharField(verbose_name="Отчество", max_length=20, blank=True)
    Post = models.CharField(verbose_name="Должность", max_length=60, blank=True)
    Number_in = models.CharField(verbose_name="Телефон внутренний", max_length=5, blank=True)
    Number_ext = models.CharField(verbose_name="Телефон городской", max_length=9, blank=True)
    #Link = models.ForeignKey(Location, verbose_name="Размещение", to_field="id", blank=True, null=True)


    def __str__(self):
        return self.SurName + self.FirstName + self.Patronymic

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'