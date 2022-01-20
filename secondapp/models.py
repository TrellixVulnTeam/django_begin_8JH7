from calendar import month
from datetime import date
from re import T
from django.db import models

# Create your models here.


class Curriculum(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    cnt = models.IntegerField()


class ArmyShop(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.TextField(null=True)
    name = models.TextField(null=True)

    class Meta:
        db_table = 'army_shop'
        managed = False
        # ordering = ['-id', name] -는 내림차순
