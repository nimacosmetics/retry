from django.urls import path

from . import views

app_name = 'lotion'
urlpatterns = [
    path('', views.index, name='')
]
