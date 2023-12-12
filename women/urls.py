from django.urls import path

from . import views
urlpatterns = [

    path('', views.women, name='women')
]
