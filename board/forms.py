from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']

class CreateBoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'

