from django.shortcuts import render
from django.views.generic import TemplateView

import json
from django.http import JsonResponse
from games.models import GameScore
# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class GameScoresView(TemplateView):
    template_name = 'game-scores.html'
    #this is where i left off!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def get_context_data(self, **kwargs):
        context = super(GameScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
        return context

def record_score(request):
    data = json.loads(request.body)

    user_name = data["user-name"]
    game = data["game"]
    score = data["score"]

    new_score = GameScore(user_name=user_name, game=game, score=score)
    new_score.save()

    response = {
        "success": True
    }