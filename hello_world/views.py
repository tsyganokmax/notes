from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


def index(request):
    context = {'book': Book.objects.all()}
    return render(request, 'base.html', context)
