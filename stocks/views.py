from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json

def home(request):

    news_api = requests.get("https://api.iex.cloud/v1/data/CORE/NEWS?last=15&token=pk_8d7f88195da14dc396d5f8a2521a0624")
    news = json.loads(news_api.content)

    content = {'news': news}

    return render(request, 'stocks/home.html', content)

def search(request):
    try:
        word = request.GET.get('word')[:4]

        stock_api = requests.get("https://api.iex.cloud/v1/data/core/quote/{0}?token=pk_8d7f88195da14dc396d5f8a2521a0624".format(word))
        stock = json.loads(stock_api.content)[0]

        news_api = requests.get("https://api.iex.cloud/v1/data/core/news/{0}?limit=6&token=pk_8d7f88195da14dc396d5f8a2521a0624".format(word))
        news = json.loads(news_api.content)
    except Exception as e:
        stock = ""

    content = {'stock': stock, 'news' : news}


    return render(request, "stocks/search.html", content)