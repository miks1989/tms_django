import datetime

import requests
from django.shortcuts import render

from catdog.models import AnimalImage
from src.settings import URL_FOR_CATS, URL_FOR_DOGS


def catdog_view(request):
    if request.method == "GET":
        return render(request, 'catdog.html')
    if request.method == "POST":
        session.
        if 'cat' in request.POST:
            responce = requests.get(URL_FOR_CATS)
            responce_dict = responce.json()
            url = responce_dict[0]['url']
            content = {'url': url}
            type_img = url.split('.')[-1]
            AnimalImage.objects.create(url=url, species=AnimalImage.CHOICES_SP[0][0],
                                       created_at=datetime.datetime.now(), type=type_img)
        elif 'dog' in request.POST:
            responce = requests.get(URL_FOR_DOGS)
            responce_dict = responce.json()
            url = responce_dict['message']
            content = {'url': url}


            # type_img = url.split('.')[-1]
            # AnimalImage.objects.create(url=url, species=AnimalImage.CHOICES_SP[1][0],
            #                            created_at=datetime.datetime.now(), type=type_img)
            # animal = AnimalImage(url=url, species=AnimalImage.CHOICES_SP[1][0],
            #                      created_at=datetime.datetime.now(), type=type_img)
            # animal.save()
        else:
            raise AttributeError('are you try to hack?')
        return render(request, 'pet.html', context=content)


def save_catdog(request):
    if request.method == "POST":
        pass
