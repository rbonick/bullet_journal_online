from django.shortcuts import render

__author__ = 'rbonick'


def index(request):
    return render(request, 'index.html', {
    })