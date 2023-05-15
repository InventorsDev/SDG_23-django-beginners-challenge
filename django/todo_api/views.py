from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        #Get all tasks
        pass
    
    elif request.method == 'POST':
        #crate a task
        pass
    
@api_view(['GET', 'DELETE', 'PUT'])
def task_detail(request):
    if request.method == 'GET':
        #Get one task
        pass
    
    elif request.method == 'PUT':
        #Update one task
        pass
    
    elif request.method == 'DELETE':
        #Delete one task
        pass
    
@api_view(['PUT'])
def task_complete(request):
    if request.method == 'PUT':
        #Update field completed of task to true
        pass