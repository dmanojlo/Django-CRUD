# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime

now = datetime.datetime.now()

class Izdano(models.Model):

    status_choices = (
        ('izdano', 'izdano'),
        ('vraćeno', 'vraćeno'),
    )

    redni_br = models.AutoField(primary_key=True)
    naziv_imovine = models.CharField(max_length=50, blank=True, null=True)
    barkod = models.CharField(max_length=50, blank=True, null=True)
    preuzeo = models.CharField(max_length=50, blank=True, null=True)
    predao = models.CharField(max_length=50, blank=True, null=True)
    datum = models.CharField(max_length=50,default=now.strftime('%d.%m.%Y'))
    status = models.CharField(max_length=20, default='izdano',choices=status_choices)

    class Meta:
        db_table = 'izdano'
