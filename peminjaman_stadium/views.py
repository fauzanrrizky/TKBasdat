from django.shortcuts import render

def peminjaman_stadium(request):
    return render(request, 'peminjaman_stadium.html')
