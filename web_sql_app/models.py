from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Cards(models.Model):
    cards = models.CharField(max_length=50)
    fio = models.CharField(db_column='FIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ntab = models.CharField(max_length=10, blank=True, null=True)
    amcom = models.DecimalField(db_column='AMCOM', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    fcard = models.IntegerField(blank=True, null=True)
    ncard = models.IntegerField(blank=True, null=True)
    rowver = models.BinaryField(blank=True, null=True)
    uuid = models.CharField(db_column='UUID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    vid = models.IntegerField(db_column='Vid')  # Field name made lowercase.
    kolall = models.IntegerField(db_column='KolAll', blank=True, null=True)  # Field name made lowercase.
    kol = models.IntegerField(db_column='Kol', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARDS'


class Sale(models.Model):
    ntab = models.CharField(max_length=10)
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    amcom = models.DecimalField(db_column='AMCOM', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kassid = models.IntegerField(blank=True, null=True)
    sum_gp = models.DecimalField(db_column='SUM_GP', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    iactive = models.SmallIntegerField(db_column='IACTIVE', blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    fcard = models.IntegerField(blank=True, null=True)
    ncard = models.IntegerField(blank=True, null=True)
    vid = models.IntegerField(db_column='Vid', blank=True, null=True)  # Field name made lowercase.
    kol = models.IntegerField(db_column='Kol', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.fcard


    class Meta:
        managed = False
        db_table = 'SALE'
        unique_together = (('ntab', 'id'),)


class Talon(models.Model):
    vid = models.IntegerField(db_column='Vid')  # Field name made lowercase.
    name = models.CharField(max_length=25)
    use_kol = models.SmallIntegerField(db_column='Use_Kol', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Talon'


