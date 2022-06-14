from .models import *
from rest_framework import serializers

class MyAppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyAppUser
        fields = ['id','user','house_no','block_no','national_id']
        #skipped image for now


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id','block_no','block_capacity']
        #skipped image for now

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id','house_no','block_no', 'occupied', 'rent', 'size', 'status']
        #skipped image for now

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','payment_id','amount', 'house_no', 'date', 'month', 'year','username','national_id']
        #skipped image for now