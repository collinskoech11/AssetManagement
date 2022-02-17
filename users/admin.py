from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
class MyAppUserAdmin(admin.ModelAdmin):
    list_display = ('user','house_no','national_id')

class HouseAdmin(admin.ModelAdmin):
    list_display = ('house_no','rent','status','size','block_no')

class BlockAdmin(admin.ModelAdmin):
    list_display = ('block_no','capacity')
    search_fields = ('block_no',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'username','house_no','month')

admin.site.register(MyAppUser, MyAppUserAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Sale)