from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('optimizacion/', views.optimizacion, name='optimizacion'),
    path('calculos/', views.calculos, name='calculos'),
]