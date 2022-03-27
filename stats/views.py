import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import forms, services

# Create your views here.
class Index(TemplateView):
    def get(self, request):
        form = forms.PlayerForm()
        tag = request.GET.get('tag')
        if tag:
            return redirect(reverse('player', kwargs={'tag':tag}))
        else:
            return render(request, 'index.html', {'form': form})

class Player(TemplateView):
    def get(self, request, tag):
        player_info = services.get_player_info(tag)
        if player_info == "error":
            return render(request, "player_not_found.html")
        else:
            player_info = json.loads(player_info)
            context = {
                'name' : player_info["name"],
                'expLevel' : player_info["expLevel"],
                'trophies' : player_info["trophies"],
            }

            return render(request, "player.html", context)

class PlayerBattles(TemplateView):
    def get(self, request, tag):
        battle_history = services.get_player_battles(tag)

        if battle_history == "error":
            return render(request, "player_not_found.html")
        else:
            battle_history = json.loads(battle_history)
            context = {'battle_history' : battle_history}
            return render(request, "battle_history.html", context)

class CardsPage(TemplateView):
    def get(self, request):
        cards_list = services.get_cards()
        return HttpResponse(cards_list, content_type="application/json")
