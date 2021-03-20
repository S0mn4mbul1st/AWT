from django.conf import settings
from django.contrib import admin
from .views import item_list
from django.urls import path, include

app_name = 'core'

urlpatterns = [
    path('', item_list, name = 'item-list')
]

