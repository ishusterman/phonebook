from django.conf.urls import url, include


from django.contrib import admin
from book import admin

from . import views

urlpatterns = [
    url(r'^$', views.book, name='book'),

]