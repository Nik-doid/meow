# models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    roll_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    parents_number = models.CharField(max_length=15, default='')
    registered_classes = models.ManyToManyField('Class', related_name='registered_students', blank=True)

    def __str__(self):
        return str(self.roll_no)

class Class(models.Model):
    roll_no = models.IntegerField(unique=True)
    name = models.CharField(_('Name'), max_length=255)
    age = models.IntegerField(default=0)
    parents_number = models.CharField(_('Parents Number'), max_length=15)

    def __str__(self):
        return f"{self.__class__.__name__} - {self.name}"

