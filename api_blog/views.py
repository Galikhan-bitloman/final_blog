from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import PostSerializer, TaskSerializer
from .models import Post, Task


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(data=request.data, instance=tasks)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE', "GET"])
def taskDelete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response('Item deleted')