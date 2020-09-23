from django.contrib import admin
from .models import Todo

# Register your models here.

# Register your models here.``
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    # list_display = ['name', 'status', 'reg_date','end_date','del_yn','group']
    pass
시리얼 라이즈로 만들래요!!