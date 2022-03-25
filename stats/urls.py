from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cards/', views.CardsPage.as_view(), name='cards-page'),
]
