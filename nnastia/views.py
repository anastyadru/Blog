from django.shortcuts import render
from .models import Nnastia


def nnastia_index(request):
    nnastias = Nnastia.objects.all()
    context = {
        'nnastias': nnastias
    }
    return render(request, 'nnastia_index.html', context)


def nnastia_detail(request, pk):
    nnastia = Nnastia.objects.get(pk=pk)
    context = {
        'nnastia': nnastia
    }
    return render(request, 'nnastia_detail.html', context)