from django.shortcuts import render

def task_view(request):
    dynamic_data = {'message': 'Hello from Django!'}
    return render(request, 'myapp/task.html', context=dynamic_data)

# Create your views here.
