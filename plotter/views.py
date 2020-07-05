from django.shortcuts import render
import asyncio

def index(request):
    return render(request, 'plotter/index.html')

def stock(request, stock_name):
    return render(request, 'plotter/stock.html', {
        'stock_name': stock_name
    })