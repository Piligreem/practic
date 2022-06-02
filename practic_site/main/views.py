from django.shortcuts import render
from django.http import HttpResponse


def main_view(request):
    # return HttpResponse('<h1>Hello world!<h1>')
    return render(request, 'main/index.html')


def cart_view(request):
    pass


