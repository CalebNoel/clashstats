from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import services

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class CardsPage(TemplateView):
    def get(self, request):
        cards_list = services.get_cards()
        return HttpResponse(cards_list, content_type="application/json")
