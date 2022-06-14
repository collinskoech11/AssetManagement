
from django.db import models
from django.contrib.auth.models import User

class MyAppUser( models.Model ) :
    def __unicode__( self ) :
       return self.user.username
    user    = models.ForeignKey( User, on_delete=models.CASCADE )
    house_no = models.CharField(max_length=255, null=True, unique=True)
    block_no = models.CharField(max_length=255, null=True)
    national_id  = models.IntegerField(null=True)



# Create your models here.


class Block(models.Model):
    block_no = models.CharField(max_length=255, primary_key=True)
    capacity = models.IntegerField()

class House(models.Model):
    house_no = models.CharField(max_length=255, primary_key=True)
    block_no = models.ForeignKey( Block, on_delete=models.CASCADE )
    occuppied = models.BooleanField(default=False)
    rent = models.IntegerField()
    size = models.CharField(max_length=255)
    status = models.CharField(max_length=255)


class Payment(models.Model):
    payment_id = models.IntegerField( primary_key=True, auto_created=True)
    amount = models.IntegerField()
    house_no = models.ForeignKey(House, on_delete=models.CASCADE)
    date = models.IntegerField()
    month = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    username = models.CharField(max_length=255)
    national_id = models.IntegerField()

class Sale(models.Model):
    item = models.CharField(max_length=100)
    price = models.FloatField()
 
    def __str__(self):
        return str(self.item)