import datetime

import requests
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from catdog.forms import PetFilterForm
from catdog.models import AnimalImage
from src.settings import URL_FOR_CATS, URL_FOR_DOGS, EMAIL_HOST_USER

import logging

logger = logging.getLogger(__name__)


def catdog_view(request):
    if request.method == "GET":
        data = {'form': PetFilterForm()}
        return render(request, 'catdog.html', data)
    if request.method == "POST":
        request.session.set_expiry(30)
        if 'cat' in request.POST:
            responce = requests.get(URL_FOR_CATS)
            responce_dict = responce.json()
            url = responce_dict[0]['url']
            content = {'url': url}
            type_img = url.split('.')[-1]
            data_for_session = {'url': url,
                                'species': AnimalImage.CHOICES_SP[0][0],
                                'type': type_img}
            request.session['data_for_session'] = data_for_session
            # type_img = url.split('.')[-1]
            # AnimalImage.objects.create(url=url, species=AnimalImage.CHOICES_SP[0][0],
            #                            created_at=datetime.datetime.now(), type=type_img)
        elif 'dog' in request.POST:
            responce = requests.get(URL_FOR_DOGS)
            responce_dict = responce.json()
            url = responce_dict['message']
            content = {'url': url}
            type_img = url.split('.')[-1]
            data_for_session = {'url': url,
                                'species': AnimalImage.CHOICES_SP[1][0],
                                'type': type_img}
            request.session['data_for_session'] = data_for_session

            # type_img = url.split('.')[-1]
            # AnimalImage.objects.create(url=url, species=AnimalImage.CHOICES_SP[1][0],
            #                            created_at=datetime.datetime.now(), type=type_img)
        else:
            raise AttributeError('are you try to hack?')
        return render(request, 'pet.html', context=content)


def save_catdog(request):
    if request.method == "POST":
        data_for_write = request.session['data_for_session']
        AnimalImage.objects.create(url=data_for_write['url'],
                                   species=data_for_write['species'],
                                   type=data_for_write['type'])
        data = {'url': data_for_write['url']}
        return render(request, 'petsaved.html', context=data)


def send_image_to_email(request):
    url = request.POST.get('url_for_image')
    mail_for_send = request.POST.get('mail')
    send_mail(
        "Subject here - cool image",
        f"Here is the link to image - {url}",
        EMAIL_HOST_USER,
        [mail_for_send],
        fail_silently=False,
    )
    return render(request, 'success_send_mail.html', {'url': url})


def pet_filter(request):
    if request.method == 'POST':
        form = PetFilterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            # pets = AnimalImage.objects.filter(species=data.get('pet'), type=data.get('type_img'))
            pets = AnimalImage.objects.filter(Q(species=data.get('pet')) &
                                              Q(type=data.get('type_img')))
            logger.info(f'hello {pets}')
            return render(request, 'pet_filter.html', {"pets": pets})
