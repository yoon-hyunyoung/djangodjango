from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Students(request):
    return render(request, 'yoonproject/Students.html')