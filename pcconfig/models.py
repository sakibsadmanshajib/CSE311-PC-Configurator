from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PC(models.Model):
    cpu = models.ForeignKey('CPU', on_delete=models.CASCADE)
    ram = models.ForeignKey('RAM', on_delete=models.CASCADE)
    gpu = models.ForeignKey('GPU', on_delete=models.CASCADE)
    motherboard = models.ForeignKey('Motherboard', on_delete=models.CASCADE)
    storage = models.ForeignKey('Storage', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class CPU(models.Model):
    brand = models.CharField(max_length=64)
    family = models.CharField(max_length=64)
    sku = models.CharField(max_length=64)
    speed = models.DecimalField(max_digits=5, decimal_places=2)
    cache = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class GPU(models.Model):
    brand = models.CharField(max_length=64)
    family = models.CharField(max_length=64)
    chip = models.CharField(max_length=64)
    vram = models.IntegerField()
    manufacturer = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class RAM(models.Model):
    manufacturer = models.CharField(max_length=64)
    Type = models.CharField(max_length=64)
    capacity = models.IntegerField()
    speed = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Motherboard(models.Model):
    brand = models.CharField(max_length=64)
    motherboard = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Storage(models.Model):
    brand = models.CharField(max_length=64)
    protocol = models.CharField(max_length=64)
    capacity = models.IntegerField()
    connector = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)