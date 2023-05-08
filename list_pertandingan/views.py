from django.shortcuts import render

def list_pertandingan(request):
    return render(request, 'list_pertandingan.html')

def list_pertandingan_manajer(request):
    return render(request, 'list_pertandingan_manajer.html')

def list_pertandingan_penonton(request):
    return render(request, 'list_pertandingan_penonton.html')
