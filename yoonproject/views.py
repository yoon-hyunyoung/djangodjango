from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import EPLSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import EPL
from django.urls import path, include

@api_view(['GET'])
def EPLView(request):
    if request.method == 'GET':
        e = EPL.objects.all()
        serializer = EPLSerializer(e, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EPLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Create your views here.
