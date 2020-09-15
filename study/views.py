from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Students, Scores
from .serializers import StudentSerializer, ScoreSerializer
from rest_framework.response import Response

class StudentView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class ScoreView(viewsets.ModelViewSet):
    queryset = Scores.objects.all()
    serializer_class = ScoreSerializer

# class StudentView(APIView):
#     def get(self, request):
#          qs = Students.objects.all()
#          Serializer = StudentSerializer(qs, many=True)
#          return Response(Serializer.data)
#     def post(self, request):
#         Serializer = StudentSerializer(data=request.data)
#         if Serializer.is_valid():
#             Serializer.save()
#             return Response(Serializer.data, status=status.HTTP_201_CREATED)
#         return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentDetailView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Students, pk=pk)

#     def get(self, request, pk):
#         qs = self.get_object(pk)
#         Serializer = StudentSerializer(qs)
#         return Response(Serializer.data)

#     def put(self, request, pk):
#         qs = self.get_object(pk)
#         Serializer = StudentSerializer(qs, data=request.data)
#         if Serializer.is_valid():
#             Serializer.save()
#             return Response(Serializer.data)
#         return Response(Serializer.errors, status=400)

#     def delete(self, request, pk):
#         qs = self.get_object(pk)
#         qs.delete()
#         return Response(status=204)


#@api_view(['GET', 'POST'])
# def StudentView(request):
#     if request.method == 'GET':
#         qs = Students.objects.all()
#         serializer = StudentSerializer(qs, many=True)
#         return Response(serializer.data)
#     elif request.method =='POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def StudentDetailView(request, id):
#     qs = get_object_or_404(Students, pk=id)
#     #상세조회
#     if request.method == 'GET':
#         serializer = StudentSerializer(qs)
#         return Response(serializer.data)
#         #수정
#     elif request.method =="PUT":
#         serializer = StudentSerializer(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#         #삭제
#     elif request.method == 'DELETE':
#         qs.delete()
#         return Response(status=404)

# class ScoreView(APIView):
#     def get(self, request):
#         sc = Scores.objects.all()
#         Serializer = ScoreSerializer(sc, many=True)
#         return Response(Serializer.data)
#     def post(self, request):
#         Serializer = ScoreSerializer(data=request.data)
#         if Serializer.is_valid():
#             Serializer.save()
#             return Response(Serializer.data, status=status.HTTP_201_CREATED)
#         return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ScoreDetailView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Scores, pk=pk)

#     def get(self, request, pk):
#         sc = self.get_object(pk)
#         Serializer = ScoreSerializer(sc)
#         return Response(Serializer.data)

#     def put(self, request, pk):
#         sc = self.get_object(pk)
#         Serializer = ScoreSerializer(sc, data=request.data)
#         if Serializer.is_valid():
#             Serializer.save()
#             return Response(Serializer.data)
#         return Response(Serializer.errors, status=400)

#     def delete(self, request, pk):
#         sc = self.get_object(pk)
#         sc.delete()
#         return Response(status=204)






# @api_view(['GET', 'POST'])
# def ScoreView(request):
#     qs = Scores.objects.all()
#     if request.method == 'GET':     
#         serializer = ScoreSerializer(qs, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ScoreSerializer(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def ScoreDetailView(request, id):
#     qs = get_object_or_404(Scores, pk=id)
#     if request.method == 'GET':
#         serializer = ScoreSerializer(qs)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ScoreSerializer(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         serializer = ScoreSerializer(qs, data=request.data)
#         qs.delete()
#         return Response(status=404)