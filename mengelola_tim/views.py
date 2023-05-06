from django.shortcuts import render

def index(request):
    return render(request, 'mengelola_tim.html')
