import requests
from django.shortcuts import render


def catdog_view(request):
    if request.method == "GET":
        return render(request, 'catdog.html')
    if request.method == "POST":
        if 'cat' in request.POST:
            responce = requests.get('https://api.thecatapi.com/v1/images/search')
            responce_dict = responce.json()
            url = responce_dict[0]['url']
            content = {'url': url}
        elif 'dog' in request.POST:
            responce = requests.get('https://dog.ceo/api/breeds/image/random')
            responce_dict = responce.json()
            url = responce_dict['message']
            content = {'url': url}
        else:
            raise AttributeError('are you try to hack?')
        return render(request, 'pet.html', context=content)
