from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
# 연고지
class EPLGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True)
    del_yn = models.BooleanField(default=False)
    def __str__(self):
        return self.name

CHOICE = [
    ("EPL","EPL"),("EFL","EFL"),("리그1","리그1")
]
        
# 1,2,3부 리그 status 팀들
class EPL(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=CHOICE)
    reg_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank=True)
    del_yn = models.BooleanField(default=False)
    score = models.IntegerField(blank=True)
    win = models.IntegerField(blank=True)
    draw = models.IntegerField(blank=True)
    lose = models.IntegerField(blank=True)
    group = models.ForeignKey(EPLGroup, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name
# 즐겨찾기
class BigmatchGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Bigmatch(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    memo = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(BigmatchGroup, on_delete=models.CASCADE)
    def __str__(self):
        return self.name