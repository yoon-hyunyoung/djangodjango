from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Students, Scores
from .serializers import StudentSerializer, ScoreSerializer
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def StudentView(request):
    if request.method == 'GET':
        qs = Students.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def StudentDetailView(request, id):
    qs = get_object_or_404(Students, pk=id)
    #상세조회
    if request.method == 'GET':
        serializer = StudentSerializer(qs)
        return Response(serializer.data)
        #수정
    elif request.method =="PUT":
        serializer = StudentSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        #삭제
    elif request.method == 'DELETE':
        qs.delete()
        return Response(status=404)

@api_view(['GET'])
def ScoreView(request):
    qs = Scores.objects.all()
    serializer = ScoreSerializer(qs, many=True)
    return Response(serializer.data)