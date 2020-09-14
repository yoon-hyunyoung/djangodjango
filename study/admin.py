from django.contrib import admin
from .models import Students, Scores
# Register your models here.
@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'email']

@admin.register(Scores)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'math', 'science', 'english']