from django.shortcuts import render

def home(request):
    return render(request, 'greetings/home.html')

def greet(request, name):
    context = {'name': name}
    return render(request, 'greetings/greeting.html', context)