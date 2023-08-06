from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json

def home(request):

    stock_api = requests.get("https://api.iex.cloud/v1/data/core/quote/goog?token=pk_8d7f88195da14dc396d5f8a2521a0624")
    stock = json.loads(stock_api.content)

    content = {'stock': stock}

    return render(request, 'stocks/home.html', content)

def search(request):
    word = request.GET.get('word')
    stock_api = requests.get("https://api.iex.cloud/v1/data/core/quote/{0}?token=pk_8d7f88195da14dc396d5f8a2521a0624".format(word[:4]))

    stock = json.loads(stock_api.content)

    content = {'stock' : stock}
    return render(request, "stocks/search.html", content)