from django.db import models
from django.conf import settings
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=150)
    mail = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo_url =  models.ImageField(blank=True,upload_to='users_profile')

class WorkExperience(models.Model):
    date_ini = models.DateTimeField()
    date_fin = models.DateTimeField()
    company = models.BigIntegerField()
    resume = models.CharField(max_length=2000)
    skill = models.CharField(max_length=1000)
    results = models.CharField(max_length=500)

class Studies(models.Model):
    date_ini = models.DateTimeField()
    date_fin = models.DateTimeField()
    school = models.BigIntegerField()
    grade = models.CharField(max_length=2000)
    career = models.CharField(max_length=1000)

class Company(models.Model):
    name = models.CharField(max_length=1000)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class School(models.Model):
    name = models.CharField(max_length=1000)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Courses(models.Model):
    name = models.CharField(max_length=100)
    by = models.CharField(max_length=100)
    date = models.DateField()

