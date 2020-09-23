from django.contrib import admin
from .models import EPL

# Register your models here.``
@admin.register(EPL)
class EPLAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'reg_date','end_date','del_yn']


    
