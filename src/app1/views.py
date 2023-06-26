import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect


def get_data(request):
    data = datetime.datetime.now()
    return HttpResponse(data)


def two_pow(request, number, power):
    result = int(number) ** power
    return HttpResponse(f'{number} ** {power} = {result}')


def hello_admin(request):
    return HttpResponse('hello admin')


def hello_guest(request, name):
    return HttpResponse(f'hello {name}')


def hello_user(request, user):
    if user == 'admin':
        return redirect('admin')
    else:
        return redirect('hello_guest123', name=user)


def my_word(request, word):
    if len(word) % 2:
        return redirect('get_time')
    else:
        return HttpResponse(f'{word[::2]}')


def login(request):
    if request.method == "POST":
        pass
    else:
        name2 = request.GET.get('name1')
        return redirect('success', name10=name2)


def success(request, name10):
    return HttpResponse("hello" + name10)


def add_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        return HttpResponse(f'name - {name}, lastname - {lastname}, age - {age}')
    else:
        pass
