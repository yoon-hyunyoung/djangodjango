from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from .models import Students, Scores
from .serializers import StudentSerializer, ScoreSerializer
from rest_framework.response import Response

# class StudentView(viewsets.ReadOnlyModelViewSet):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer

# class ScoreView(viewsets.ReadOnlyModelViewSet):
#     queryset = Scores.objects.all()
#     serializer_class = ScoreSerializer





class StudentView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name=name)
        return qs
    @action(detail=False, methods=['GET'])
    def seoul(self, request):
        qs = self.get_queryset().filter(address__contains='서울')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PUT'])
    def init(self, request, pk):
        instance = self.get_object()
        instance.address = ""
        instance.email = ""
        instance.save(update_fields=['address', 'email'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ScoreView(ModelViewSet):
    queryset = Scores.objects.all() #전체데이터를 조회하는
    serializer_class = ScoreSerializer

    # 오버라이딩
    def get_queryset(self):
        #Scores.objects.all()
        qs = super().get_queryset() # SELECT * FROM scores

        name = self.request.query_params.get('name')
        math = self.request.query_params.get('math')
        science = self.request.query_params.get('science')
        english = self.request.query_params.get('english')
        order = self.request.query_params.get('order')

        if name:
            qs = qs.filter(name=name) # SELECT * FROM scores WHERE name = name
        if math:
            qs = qs.filter(math__gte=math)
        if science:
            qs = qs.filter(math__gte=science)
        if english:
            qs = qs.filter(math__gte=english)
        if order:
            qs = qs.order_by(order)

        return qs

    #PUT, DETAIL GET, DELETE (PK)
    #LIST, LIST 0, 1, >=
    @action(detail=False, methods=['GET'])
    def top(self, request):
        qs = self.get_queryset().filter(math__gte=80, english__gte=80, science__gte=80)
        #ScoreSerializer
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)




    # def science(self, request):
    #     qs = self.get_queryset().filter(science__gte=80)
    #     serializer = self.get_serializer(qs, many=True)
    #     return Response(serializer.data)
    # def english(self, request):
    #     qs = self.get_queryset().filter(english__gte=80)
    #     serializer = self.get_serializer(qs, many=True)
    #     return Response(serializer.data)

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