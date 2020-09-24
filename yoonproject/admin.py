from django.contrib import admin
from .models import EPL, EPLGroup, Bigmatch, BigmatchGroup

# Register your models here.``
@admin.register(EPL)
class EPLAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'reg_date', 'end_date', 'del_yn', 'group']
@admin.register(EPLGroup)
class EPLGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'reg_date', 'del_yn']
@admin.register(Bigmatch)
class EPLGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'memo', 'reg_date', 'group']
@admin.register(BigmatchGroup)
class EPLGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'reg_date']


    
