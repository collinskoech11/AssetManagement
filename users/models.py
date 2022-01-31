from django.db import models

# Create your models here.
class House(models.Model):
    house_no = models.CharField(max_length=255, primary_key=True)
    block = models.CharField(max_length=20)
    rent = models.IntegerField()
    size = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

class Block(models.Model):
    block_no = models.CharField(max_length=255, primary_key=True)
    capacity = models.IntegerField()

class Payment(models.Model):
    payment_id = models.IntegerField( primary_key=True, auto_created=True)
    amount = models.IntegerField()
    date = models.IntegerField()
    month = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    username = models.CharField(max_length=255)
    national_id = models.IntegerField()