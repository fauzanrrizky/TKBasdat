from django.shortcuts import render

def list_pertandingan(request):
    return render(request, 'list_pertandingan.html')
