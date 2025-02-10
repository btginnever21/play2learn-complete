from django.db import models

from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class GameScore(models.Model):

    MATH= "MATH"
    ANAGRAM = "ANAGRAM"

    GAME_CHOICES = [
        (MATH, "Math Game"),
        (ANAGRAM, "Anagram Game")
    ]
    user_name = models.TextField()
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.game_type} - {self.score}"
