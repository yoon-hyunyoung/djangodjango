from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, action
from .serializers import EPLSerializer
from rest_framework.response import Response
from .models import EPL

@api_view(['GET', 'POST'])
def EPLView(request):
    # if request.method == 'GET':
        qs = EPL.objects.filter()
        serializer = EPLSerializer(qs, many=True)
        return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)



# Create your views here.
def Students(request):
    return render(request, 'yoonproject/Students.html')