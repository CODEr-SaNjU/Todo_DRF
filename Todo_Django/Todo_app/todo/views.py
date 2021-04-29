from django.shortcuts import render
from django.http import HttpResponse, response
from .serializers import TodoSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Todo
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def TodoView(request):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer(queryset, many=True)
    return Response(serializer_class.data)


@api_view(['POST'])
def TodoCreate(request):
    serializer_class = TodoSerializer(data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def TodoDetails(request, pk):
    queryset = Todo.objects.get(id=pk)
    serializer_class = TodoSerializer(queryset, many=False)
    return Response(serializer_class.data)


@api_view(['POST'])
def TodoUpdate(request, pk):
    queryset = Todo.objects.get(id=pk)
    serializer_class = TodoSerializer(instance=queryset, data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def TodoDelete(request, pk):
    queryset = Todo.objects.get(id=pk)
    queryset.delete()
    return Response("finally delete data here ")
