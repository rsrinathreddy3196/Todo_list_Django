from django.shortcuts import render
from . models import Task

# Create your views here.

def home(request):
    context = {'success':False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        obj = Task(Task_details = title,  Task_description = desc)
        obj.save()
        context = {'success':True}
    return render(request, "index.html", context)


def task(request):
    alltasks = Task.objects.all()
    context = {'mytasks': alltasks}
    return render(request, "task.html", context)    
 
    