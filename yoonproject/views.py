from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from .serializers import EPLSerializer ,EPLGroupSerializer, BigmatchSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import EPL, EPLGroup, Bigmatch
from django.urls import path, include
from rest_framework.permissions import IsAuthenticated

@api_view(['DELETE'])
def EPLAllSelectDeleteView(request, seq):
        data = EPL.objects.get(seq=seq)
        if request.method == 'DELETE':
            data.delete()
            return Response()


@api_view(['GET', 'POST','DELETE'])
# @permission_classes([IsAuthenticated])
def EPLAllSelectView(request):
    if request.method == 'GET':
        data = EPL.objects.all()
        epl = EPLSerializer(data.filter(status="EPL"), many=True)
        efl = EPLSerializer(data.filter(status="EFL"), many=True)
        lg1 = EPLSerializer(data.filter(status="리그1"), many=True)
    
        return Response({
            "epl": epl.data,
            "efl": efl.data,
            "g1": lg1.data
        })
    elif request.method == 'POST':
        serializer = EPLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET','POST'])
def EPLGroupView(request):
    if request.method == 'GET':
        data = EPLGroup.objects.all()
        serializer = EPLGroupSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EPLGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
            data.delete()
            return Response()

@api_view(['GET','POST'])
def EPLView(request):
    if request.method == 'GET':
        data = EPL.objects.filter(status="EPL")
        serializer = EPLSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EPLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET','POST'])
def EFLView(request):
    if request.method == 'GET':
        data = EPL.objects.filter(status="EFL")
        serializer = EPLSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EPLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET','POST'])
def LEAGUE1View(request):
    if request.method == 'GET':
        data = EPL.objects.filter(status="리그1")
        serializer = EPLSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EPLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET','POST'])
def BigmatchView(request):
    if request.method == 'GET':
        d = Bigmatch.objects.all()
        group = request.query_params.get('group')
        if group:
            d = d.filter(group=group)
        serializer = BigmatchSerializer(d, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BigmatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'DELETE'])
def BigmatchdeleteView(request, seq):
        s = Bigmatch.objects.get(seq=seq)
        if request.method == 'DELETE':
            s.delete()
            return Response()
@api_view(['GET', 'DELETE'])
def LEAGUE1deleteView(request, seq):
        s = Bigmatch.objects.get(seq=seq)
        if request.method == 'DELETE':
            s.delete()
            return Response()           
@api_view(['GET', 'DELETE'])
def EFLdeleteView(request, seq):
        s = Bigmatch.objects.get(seq=seq)
        if request.method == 'DELETE':
            s.delete()
            return Response() 
@api_view(['GET', 'DELETE'])
def EPLdeleteView(request, seq):
        s = Bigmatch.objects.get(seq=seq)
        if request.method == 'DELETE':
            s.delete()
            return Response() 


# 뷰셋에서 사용법..
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     status = self.request.query_params.get('group')
    #     if status:
    #         qs = qs.filter(group=group)
    #     return qs

# Create your views here.