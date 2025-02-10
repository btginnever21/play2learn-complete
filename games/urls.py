from django.urls import path
from django.contrib.auth import views as auth_views
from games.views import HomeView, MathFactsView, AnagramHuntView, GameScoresView, ContactUsView, game_scores, record_score




app_name = 'games'
urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('record-score/', record_score, name="record-score"),
    path('game-scores/', GameScoresView.as_view(), name='game-scores'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='account_login'),
    
]