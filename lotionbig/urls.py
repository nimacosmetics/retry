from django.urls import path

from . import views
app_name = 'lotionbig'
urlpatterns = [
    path('', views.index, name='index')
]