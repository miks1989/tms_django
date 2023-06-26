"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app1.views import get_data, two_pow, hello_admin, hello_guest, hello_user, my_word, success, login, add_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_data, name='get_time'),
    path('two_pow/<number>/<int:power>', two_pow),
    path('hello_admin/', hello_admin, name='admin'),
    path('hello_guest/<name>', hello_guest, name='hello_guest123'),
    path('hello_user/<user>', hello_user, name='hello_user'),
    path('my_word/<word>', my_word, name='my_word'),
    path('success/<name10>', success, name='success'),
    path('login/', login, name='login'),
    path('add_user/', add_user, name='add_user'),


]
