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
from django.urls import path

from catdog.views import catdog_view, save_catdog, send_image_to_email, pet_filter
from school.views import all_groups_view, all_students_of_the_group

urlpatterns = [
    path('', catdog_view,
         name='catdog'),
    path('save_catdog123456', save_catdog,
         name='save_catdog'),
    path('send_mail', send_image_to_email,
         name='send_mail'),
    path('pet_filter', pet_filter,
         name='pet_filter'),
]
