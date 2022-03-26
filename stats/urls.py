from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('cards/', views.CardsPage.as_view(), name='cards-page'),
    path('player/<str:tag>/', views.Player.as_view(), name='player'),
]
