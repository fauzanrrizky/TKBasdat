from django.shortcuts import render

def mulai_rapat(request):
    return render(request, 'mulai_rapat.html')

def rapat_pertandingan(request):
    return render(request, 'rapat_pertandingan.html')
