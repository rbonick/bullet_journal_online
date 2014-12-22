from django.shortcuts import render

__author__ = 'rbonick'


def home(request):
    return render(request, 'base.html', {
    })