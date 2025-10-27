from django.shortcuts import render
import requests

def exchange(request):
    response = requests.get(url='https://www.cbr-xml-daily.ru/#terms"')
    return render(request, 'exchange/index.html')
