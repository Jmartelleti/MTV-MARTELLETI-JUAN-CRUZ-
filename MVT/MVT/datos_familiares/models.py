from django.db import models

class Familiar (models.Model):
    Nombre=models.CharField(max_length=64)
    Edad=models.IntegerField()
    Cumpleaños=models.DateField()




