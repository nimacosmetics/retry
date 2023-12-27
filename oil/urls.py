from django.urls import path

from . import views
app_name = 'oil'
urlpatterns = [
    path('', views.index, name='index')
]