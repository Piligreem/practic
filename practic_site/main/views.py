from django.shortcuts import render
from django.http import HttpResponse


def main_view(request):
    return HttpResponse('<h1>Hello world!<h1>')


def products_view(request):
    if request.method == 'GET':
       pass 


def categories_view(request):
    if request.method == 'GET':
        pass


def vendors_view(request):
    if request.method == 'GET':
        pass


def buy_view(request):
    if request.method == 'POST':
        pass


