from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

BIRTH_YEAR_CHOICES = range(1915, datetime.now().year)

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

class CustomUserChangeForm(UserChangeForm):
    password = None
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'dob', 'avatar')
        widgets = {
            'dob': forms.SelectDateWidget(
                attrs={
                    'style': 'width: 31%; display: inline-block; margin: 0 1%'
                },
                years = BIRTH_YEAR_CHOICES
            )
        }

from django import forms
from .models import Review, ContactMessage, GameSession

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your review here...'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

class GameSessionForm(forms.ModelForm):
    class Meta:
        model = GameSession
        fields = ['game_type', 'game_settings', 'score']
        widgets = {
            'game_type': forms.TextInput(attrs={'class': 'form-control'}),
            'game_settings': forms.Textarea(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Views
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReviewForm, ContactForm, GameSessionForm

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Review submitted successfully!')
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'submit_review.html', {'form': form})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

def submit_game_score(request):
    if request.method == 'POST':
        form = GameSessionForm(request.POST)
        if form.is_valid():
            game_session = form.save(commit=False)
            game_session.user = request.user
            game_session.save()
            messages.success(request, 'Game score recorded!')
            return redirect('game-scores')
    else:
        form = GameSessionForm()
    return render(request, 'submit_game_score.html', {'form': form})
