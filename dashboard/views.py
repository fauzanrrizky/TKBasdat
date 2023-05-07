from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def dashboard_manajer(request):
    return render(request, 'dashboard_manajer.html')

def dashboard_panitia(request):
    return render(request, 'dashboard_panitia.html')

def dashboard_penonton(request):
    return render(request, 'dashboard_penonton.html')
