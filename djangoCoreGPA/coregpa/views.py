from django.shortcuts import render
from django.http import HttpResponse

def coreGPAView(request):
    return render(request, 'coregpa/index.html')

