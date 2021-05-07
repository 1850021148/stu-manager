from django.db import models

# Create your models here.

"""
    python manage.py makemigrations
    python manage.py migrate
    默认表名为: 应用名_类名
"""

# core
class Manager(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

class Student(models.Model):
    sno = models.CharField(primary_key=True, max_length=10)
    sname = models.CharField(max_length=10)
    sex = models.CharField(default='male', max_length=10)
    age = models.CharField(max_length=10)
    pro = models.CharField(max_length=10)
    address = models.CharField(max_length=10)

# test
class User(models.Model):
    name = models.CharField(max_length=10)
    password = models.FloatField(max_length=10)
