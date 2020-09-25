from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import EPLSerializer ,EPLGroupSerializer, BigmatchSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import EPL, EPLGroup, Bigmatch
from django.urls import path, include

@api_view(['GET','POST', 'DELETE'])
def EPLView(request):
    if request.method == 'GET':
        data = EPL.objects.filter(status="EPL")
        serializer = EPLSerializer(data, many=True)
        return Response(serializer.data)
@api_view(['GET','POST', 'DELETE'])
def EFLView(request):
    if request.method == 'GET':
        data = EPL.objects.filter(status="EFL")
        serializer = EPLSerializer(data, many=True)
        return Response(serializer.data)
@api_view(['GET','POST', 'DELETE'])
def LEAGUE1View(request):
    if request.method == 'GET':
        data = EPL.objects.filter(status="리그1")
        serializer = EPLSerializer(data, many=True)
        return Response(serializer.data)
        
    # elif request.method == 'POST':
    #     serializer = EPLSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
    # elif request.method == 'DELETE':
    #     e.delete()
    #     return Response(status=404)
@api_view(['GET','POST', 'DELETE'])
def BigmatchView(request):
    if request.method == 'GET':
        d = Bigmatch.objects.all()
        serializer = BigmatchSerializer(d, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BigmatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        d.delete()
        return Response(status=404)
# Create your views here.








# data2 = EPL.objects.filter(status="EFL")
#         serializer2 = EPLSerializer(data2, many=True)
#         return Response(serializer2.data)
#         data3 = EPL.objects.filter(status="리그1")
#         serializer3 = EPLSerializer(data3, many=True)
#         return Response(serializer3.data)