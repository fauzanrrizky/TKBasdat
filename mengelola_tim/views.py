from django.shortcuts import render

def mengelola_tim(request):
    return render(request, 'mengelola_tim.html')

def regist(request):
    return render(request, 'form_registrasi.html')