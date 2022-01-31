from django.contrib import admin
from .models import *

# Register your models here.
class HouseAdmin(admin.ModelAdmin):
    list_display = ('house_no','rent','status')

class BlockAdmin(admin.ModelAdmin):
    list_display = ('block_no','capacity')
    search_fields = ('block_no',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'username')


admin.site.register(House, HouseAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Payment, PaymentAdmin)
