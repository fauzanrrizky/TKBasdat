from django.shortcuts import render

def pembuatan_pertandingan(request):
    return render(request, 'pembuatan_pertandingan.html')

def pembuatan_pertandingan_lanjutan(request):
    return render(request, 'pembuatan_pertandingan_lanjutan.html')
