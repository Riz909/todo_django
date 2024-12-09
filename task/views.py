from datetime import datetime
import json
from urllib import response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from task.serializer import TaskSerializer
from .models import Task

# Create your views here.
def home(request):
    return render(request, 'home.html')

def getTask(request):
    status = request.GET.get('status')

    # Filter tasks based on the 'status' query parameter
    if status == 'incoming':
        tasks = Task.objects.filter(due_date__gt=datetime.today().date())  # Tasks due in the future
    elif status == 'overdue':
        tasks = Task.objects.filter(due_date__lt=datetime.today().date())  # Overdue tasks
    elif status == 'today':
        tasks = Task.objects.filter(due_date=datetime.today().date())  # Tasks due today
    else:
        # If no status or an invalid status is provided, return all tasks
        tasks = Task.objects.all()


    serializer = TaskSerializer(tasks, many=True)
    return render(request, 'todolist.html', {'tasks': serializer.data})

def addtask(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        Task.objects.create(
            title=title,
            description=description,  
            due_date=due_date,
        )
        return redirect('get.task')  
    
def deletetask(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('get.task') 

def getdescription(request, id):
    task = get_object_or_404(Task, id=id)
    context = {
        'task': task
    }
    return render(request, 'description.html', context) 

def updatetask(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
  
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')


        # update task
        task.title = title
        task.description = description
        task.due_date = due_date
        task.save()

    return redirect("get.task.description", id)