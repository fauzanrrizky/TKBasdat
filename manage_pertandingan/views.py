from django.shortcuts import render

def manage_pertandingan(request):
    return render(request, 'manage_pertandingan.html')

def peristiwa(request):
    return render(request, 'peristiwa.html')

def buat_pertandingan(request):
    return render(request, 'buat_pertandingan.html')

def akhir_musim(request):
    return render(request, 'akhir_musim.html')