from django.db import models

# Create your models here.
class reg_student(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=12)
    email = models.CharField(max_length=100, default="Null")
    date = models.DateField()

class form_data(models.Model):
    emailF = models.CharField(max_length=100)
    studentName = models.CharField(max_length=100)
    collegeName = models.CharField(max_length=100)
    websiteUsername = models.CharField(max_length=100)
    tasks = models.CharField(max_length=300)
    percent = models.CharField(max_length=3)
    date = models.CharField(max_length=20)


